# TODO: Goal๐ฏ : ๋ค์ด๋ฒ ๋ธ๋ก๊ทธ ๊ฒ์ํด ๋ง๋ค๊ธฐ(๊ฒ์์ด๋ฅผ ๋ฐ์ผ๋ฉด ๋ธ๋ก๊ทธ ๊ฒ์๋ฌผ์ ์ ๋ชฉ๊ณผ ์ฃผ์๋ฅผ ๊ฐ์ ธ์จ๋ค.)

# TODO:
# TODO: ๊ฒ์์ด๋ฅผ ๋ฐ๋๋ค.
# TODO: ๊ฒ์์ด๋ฅผ ๋ค์ด๋ฒ ๊ฒ์์ ์ ์ฉ ๋ฐ ๋ถ๋ฌ์ค๊ธฐ
# TODO: ๋ฌดํ์คํฌ๋กค์ ์ดํดํ๊ณ  ๊ฐ ๋ธ๋ก๊ทธ ๊ฒ์๋ฌผ์ ์ ๋ชฉ๊ณผ ๋งํฌ๋ฅผ ์ถ๋ ฅํ๋ค.

import requests
from bs4 import BeautifulSoup


def naver_blog_finder():
    search_word = input("๋ค์ด๋ฒ์์ ์ฐพ๊ธฐ๋ฅผ ์ํ๋ ๋ธ๋ก๊ทธ ๊ฒ์์ด๋ฅผ ์๋ ฅํ์ธ์.\n ->")
    page_nums = 1
    count = 0

    while True:
        try:
            view_page_url = f"https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start={page_nums}&query={search_word}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=1&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=61&sm=tab_hty.top&ssc=tab.view.view&ngn_country=KR&lgl_rcode=11200103&fgn_region=&fgn_city=&lgl_lat=37.448775&lgl_long=126.7319911&abt=&_callback=viewMoreContents "
            view_page = requests.get(view_page_url)
            # soup = BeautifulSoup(view_page.content, "html.parser")
            soup = BeautifulSoup(view_page.text.replace("\\", ""), "html.parser")
            for i in range(30):
                print(soup.select("a.api_txt_lines")[i].text)
                print(soup.select("a.api_txt_lines")[i]["href"])
                print("")
                count += 1
            page_nums += 30
        except:
            break

    print(f"๋ค์ด๋ฒ์ {search_word}๊ด๋ จ ๋ธ๋ก๊ทธ ๊ธ์ด ๋๋ฌ์ต๋๋ค.")
    print(f"์ ์ฒด ๊ธ ์๋ {count}์๋๋ค")

naver_blog_finder()
