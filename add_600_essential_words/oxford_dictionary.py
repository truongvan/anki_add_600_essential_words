import os
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from tempfile import NamedTemporaryFile
from aqt import mw

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) "\
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
}

def parts_of_speech_split(text:str):
    splited_text = text.split(", ")
    return splited_text[-1]

def create_audio_file_name(url:str) -> str:
    return "oxford_dictionary_" + url.split('/')[-1]

def get_audio(url:str) -> str:
    r = requests.get(url, headers=headers)
    tf_name = None
    media_name = create_audio_file_name(url)
    full_path_media = os.path.join(mw.col.media.dir(), media_name)
    if not os.path.exists(full_path_media):
        with NamedTemporaryFile(delete=False) as tf:
            tf_name = tf.name
            for i in r.iter_content(chunk_size=128):
                tf.write(i)
        with open(tf_name, 'rb') as f:
            mw.col.media.write_data(media_name, f.read())
        os.unlink(tf_name)
    return f"[sound:{media_name}]"



def get_word(word:str, part_of_speech:str, url:str = None):
    word_detail = {
        'IPA': None,
        'Sound_US': None
    }
    if url is None:
        url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"
    r = requests.get(url, headers=headers)
    if r.ok:
        soup = BeautifulSoup(r.text, "html.parser")
        _parts_of_speech = parts_of_speech_split(soup.select_one("div > span.pos").text)
        if part_of_speech != _parts_of_speech:
            for tag in soup.select_one("#relatedentries > dl > dd:nth-child(2) > ul"):
                if isinstance(tag, Tag) and tag.a.span.pos: # tag is a Tag and have `pos` tag
                    _w, _pos, *__ = tag.a.span.text.split(" ")
                    if  part_of_speech == _pos:
                        href_tag_a = tag.a.get("href")
                        return get_word(word, part_of_speech, href_tag_a)
        else:
            sound_us_link = soup.select_one("div > span.phonetics > div.phons_n_am > div").get("data-src-mp3")
            word_detail['IPA'] = soup.select_one("span.phonetics > div.phons_n_am > span").text.strip('/')
            word_detail['Sound_US'] = get_audio(sound_us_link)
            return word_detail
                