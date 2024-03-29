from selenium import webdriver


class Selenium():

    def __init__(self):
        self.driver = self.getDriver()
        self.driver.get('https://www.google.com/')

    def getDriver(self):
        # googleユーザープロファイル
        options = webdriver.ChromeOptions()
        # プロファイルのパスを指定
        options.add_argument('--user-data-dir=/Users/user/Library/Application Support/Google/Chrome')
        # 使用するプロファイル(ユーザー)を指定
        options.add_argument('--profile-directory=Profile 11')
        # ブラウザーを起動
        driver = webdriver.Chrome(
            options=options,
        )

        return driver


if __name__ == '__main__':
    selenium = Selenium()
    while(1):
        pass
