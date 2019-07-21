import time
from sites.sites import Naver
from user_info import LOGIN_ID, LOGIN_PASSWORD,PETER_PAN_URL

if __name__ == "__main__":
    naver = Naver(LOGIN_ID, LOGIN_PASSWORD)
    try:
        # 1. naver login
        naver.excute_script_login(naver.ID, naver.PW)
            # 2. naver peterpan cafe 이동
        naver.move_to_new_url(PETER_PAN_URL)

        # naver.move_to_new_url('//*[@id="menuLink1106"]')

        # naver.get_to_information('//*[@id="menuLink1106"]')
        naver.get_to_information()
    finally:
        time.sleep(5)
        naver.driver.quit()
