import requests as rq
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver


login_url = "http://www.hongik.ac.kr/login.do?Refer=https://cn.hongik.ac.kr/"  # 클래스넷 접속 URL
craw_url = 'https://cn.hongik.ac.kr/stud/' 

session = rq.session()

class Compares:

    def __init__(self, id, pw):
        self.params = dict()
        self.params['m_id'] = id  # 'B611090'
        self.params['m_passwd'] = pw  # 'titanic104404'
        self.check = dict()
        if id[0] == 'B':
            if int(id[1])<=8:
                self.check["교필"] = 6
                self.check["일교"] = 2
                self.check["핵교"] = 2
                self.check['교양인정학점'] = 23
                self.check['졸업인정학점'] = 132
                self.check['과학'] = 9
                self.check['수학'] = 9
                self.check['전산'] = 0
                self.check['계 (일반과정 MSC인정학점)'] = 18
                self.check['심화과정 MSC인정학점'] = 18
                self.check['전공'] = 50
                self.check['전공기초'] = 2
                self.check['취득학점'] = 132

            elif int(id[1])<=5:
                self.check["교필"] = 6
                self.check["일교"] = 2
                self.check["핵교"] = 2
                self.check['교양인정학점'] = 20
                self.check['졸업인정학점'] = 140
                self.check['과학'] = 9
                self.check['수학'] = 9
                self.check['전산'] = 0
                self.check['계 (일반과정 MSC인정학점)'] = 18
                self.check['심화과정 MSC인정학점'] = 18
                self.check['전공'] = 50
                self.check['전공기초'] = 2
                self.check['취득학점'] = 140

    def crawling(self, ):

        # Selenium을 이용한 졸업요건 Crawling
        # 직접 클래스넷에 접속하여 졸업요건 조회 사이트로 이동
        # 이후 HTML 자체를 크롤링하여 졸업요건 Data 확보

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        chromedriver = '.\\static\\driver\\chromedriver.exe' # 나중에 경로 어떻게 설정해야하는지 알아보고 수정할 것.
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        #driver = webdriver.Chrome(chromedriver, options=options)

        output = dict()
        # 홍익대학교 클래스넷 및 졸업요건조회 사이트로 이동

        driver.get(login_url)
        driver.find_element_by_name('USER_ID').send_keys(self.params.get('m_id'))
        driver.find_element_by_name('PASSWD').send_keys(self.params.get('m_passwd'))
        driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div[2]/div/table/tbody/tr/td[2]/div/form/div/div/div[2]/button').click()

        try:
            result = driver.switch_to.alert
            print(result.text)
            if result.text[:2] =='ID':
                return -1
            result.dismiss()
        except:
            "no"

        driver.get('https://cn.hongik.ac.kr/stud/E/04000/04000.jsp')
        try:
            driver.find_element_by_xpath('//*[@id="body"]/form/div[1]/table/tbody/tr/td[5]/input[2]').click()
        except:
            self.crawling()
        driver.find_element_by_xpath('//*[@id="body"]/form/div[2]/input[2]').click()


        # HTML crawling을 통한 User의 졸업요건 data 확보
        '''
        c = BeautifulSoup(driver.page_source, 'html.parser')
        c = c.find('div', class_="table0 mato10")
        print(c)
        c = c.find('div', class_="table0 mato10")
        print(c)
        '''
        info = driver.find_element_by_xpath('//*[@id="body"]/div[5]')
        a = driver.find_element_by_xpath('//*[@id="body"]/div[7]')
        a = a.find_elements_by_class_name("center")
        info = info.find_elements_by_class_name("center")
        data = []
        for z in a:
            print(z.text)
        # data가공
        for i in info:
            data.append(i.text)
        del data[0]
        del data[2]
        data.remove("MSC")
        data = data[:-4]
        data[data.index("졸업인정학점")] = "교양인정학점"
        CultureCnt = 0
        CheckList = []
        for i in range(0,len(data)-1,2):
            if data[i][:-1] == "일교":
                if int(data[i+1]) >= self.check[data[i][:-1]]:
                    CultureCnt += 1
                    output[data[i]] = ['교양', data[i], int(data[i+1]), "충족", 'btn']
                else:
                    CheckList.append([data[i],['교양', data[i], int(data[i+1])]])
            elif data[i] == "교필":
                if int(data[i + 1]) >= self.check[data[i]]:
                    output[data[i]] = ['교양', data[i], int(data[i + 1]), "충족",'btn']
                else:
                    output[data[i]] = ['교양', data[i], int(data[i + 1]), "부족",'btn']
            elif data[i][:-1] == "핵교":
                if int(data[i+1]) >= self.check[data[i][:-1]]:
                    CultureCnt += 1
                    output[data[i]] = ['교양', data[i], int(data[i+1]), "충족", 'btn']
                else:
                    CheckList.append([data[i],['교양', data[i], int(data[i+1])]])
            elif data[i] == "교양인정학점":
                if int(data[i + 1]) >= self.check[data[i]]:
                    output[data[i]] = ['교양', data[i], int(data[i + 1]), "충족",'btn']
                else:
                    output[data[i]] = ['교양', data[i], int(data[i + 1]), "부족",'btn']
            elif data[i] == "과학" or data[i] == "수학" or  data[i] == "전산":
                if int(data[i + 1]) >= self.check[data[i]]:
                    output[data[i]] = ['MSC', data[i], int(data[i + 1]), "충족",'btn']
                else:
                    output[data[i]] = ['MSC', data[i], int(data[i + 1]), "부족",'btn']
            elif data[i] == "계 (일반과정 MSC인정학점)":
                if int(data[i + 1]) >= self.check[data[i]]:
                    output[data[i]] = ['MSC', data[i], int(data[i + 1]), "충족"]
                else:
                    output[data[i]] = ['MSC', data[i], int(data[i + 1]), "부족"]
            elif data[i][:2] == "전공":
                if int(data[i + 1]) >= self.check[data[i]]:
                    output[data[i]] = ['-', data[i], int(data[i + 1]), "충족", 'btn']
                else:
                    output[data[i]] = ['-', data[i], int(data[i + 1]), "부족", 'btn']
            elif data[i] == "취득학점":
                if int(data[i + 1]) >= self.check[data[i]]:
                    output[data[i]] = ['-', data[i], int(data[i + 1]), "충족"]
                else:
                    output[data[i]] = ['-', data[i], int(data[i + 1]), "부족"]
            elif data[i] == "졸업인정학점":
                if int(data[i + 1]) >= self.check[data[i]]:
                    output[data[i]] = ['-', data[i], int(data[i + 1]), "충족"]
                else:
                    output[data[i]] = ['-', data[i], int(data[i + 1]), "부족"]
            else:
                output[data[i]] = ['-',data[i],int(data[i+1]),'-']
            for key,value in CheckList:
                if CultureCnt >= 5:
                    output[key] = value+['부족(듣지 않아도 됨)','btn']
                else:
                    output[key] = value+['부족','btn']

        return output

