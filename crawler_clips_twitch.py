from typing import Tuple
from selenium import webdriver
import requests
import os
import time
from moviepy.editor import VideoFileClip, concatenate_videoclips
class VideoTwitch(object):
    # url = 'https://www.twitch.tv/directory/game/League%20of%20Legends/clips?range=7d'
    # video_time = 2
    # video_name = 'teste'

    def __init__(self):
        self.url = input('URL dos clips: ')
        self.video_time = int(input('Tempo maximo em minutos do video: '))
        self.video_name = input('Nome do video: ')
    
        self.driver = webdriver.Chrome('./webdriver/chromedriver')
        self.driver.get(self.url)
        time.sleep(2)

        self.video_time = self.video_time * 60
        has_language = input('Deseja setar um filtro por lingua? [N/y]: ')
        self.setLanguageTwitch(has_language)

        clips_array = self.createClipsArray()
        self.downloadClips(clips_array)
        self.driver.close()
        self.concatenateClips(clips_array)

    def createClipsArray(self):
        clips = []
        current_video_duration = 0
        
        self.downPage()

        videos_array = self.driver.find_elements_by_css_selector('div[data-a-target|=clips-card]')
        
        for idx, video in enumerate(videos_array):
            clips.append({
                'name': video.find_element_by_css_selector('h3').text,
                'channel': video.find_element_by_css_selector('p').text,
                'duration': video.find_elements_by_css_selector('div div p')[2].text,
                'create_by': video.find_elements_by_css_selector('div div p')[1].text.split(' ')[-1],
                'views': video.find_elements_by_css_selector('div div p')[3].text,
                'url': video.find_element_by_css_selector('div div div a').get_attribute('href')
            })
            current_video_duration = current_video_duration + self.durationInSeconds(clips[idx]['duration'])  

            if current_video_duration >= self.video_time:
                return clips

    def durationInSeconds(self, _duration: str):
        _duration = _duration.split(':')
        return (int(_duration[0]) * 60) + int(_duration[1])

    def downloadClips(self, _clips_array):        
        path = os.path.join(os.getcwd() + '/clips', self.video_name)
        existPath = os.path.exists(path)
        if existPath == False:
            os.mkdir(path)

        xpath_clip = '//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/video'

        for idx, clip in enumerate(_clips_array):
            self.driver.get(clip['url'])
            time.sleep(2)
            link_video_download = self.driver.find_element_by_xpath(xpath_clip).get_attribute('src')
            file_download = requests.get(link_video_download, allow_redirects=True)
            open('./clips/{}/{}{}.mp4'.format(self.video_name, self.video_name, idx), 'wb').write(file_download.content)

    def concatenateClips(self, _clips_array):
        concatenate_array = []
        for idx in range(len(_clips_array)):
            concatenate_array.append(
                VideoFileClip('./clips/{}/{}{}.mp4'.format(self.video_name, self.video_name, idx)).resize(width=1920)
                )
            concatenate_array.append(
                VideoFileClip('./clips/tran_video.mp4').resize(width=1920)
                )
        final_clip = concatenate_videoclips(concatenate_array)
        final_clip.write_videofile('./clips/{}/{}-conc.mp4'.format(self.video_name, self.video_name))
    
    def setLanguageTwitch(self, _has_language):
        if _has_language == 'y' or _has_language == 'Y':
            language_button = self.driver.find_elements_by_css_selector('div[data-toggle-balloon-id]')[1]
            language_button.click()
            print('Selecione o filtro de lingua: ')

            array_languages = self.driver.find_elements_by_css_selector('div[data-language-code]')
            for idx in range(len(array_languages)):
                print('Selecione {} para {}'.format(idx, array_languages[idx].text))

            id_language = int(input(''))
            array_languages[id_language].click()

        elif _has_language == 'N' or _has_language == 'n' or _has_language == '':
            return
        
        else:
            has_language = input('Deseja setar um filtro por lingua? [N/y]')
            self.setLanguageTwitch(has_language)
    
    def downPage(self):
        SCROLL_PAUSE_TIME = 0.5

        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(SCROLL_PAUSE_TIME)

            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
