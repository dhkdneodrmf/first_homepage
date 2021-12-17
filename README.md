# Django SSAC 실습 홈페이지

### member app 1개 생성

현재 jyr.ideadream.co.kr:7000 으로 접속

#### /dhkdneod/ok1  
1~10 숫자가 접속 시 임의로 바뀌며 5이하면 하류층, 5이상이면 상류층 표시

#### /dhkdneod/send 
폼 전송 실습, 보낼시 recive에서 post로 전송

#### /dhkdneod/join 
회원가입 양식을 작성하면 다음 회원가입 완료 페이지에 정보가 나타나게함. 부트스트랩 이용. DB연동X

#### /dhkdneod/join2 
회원가입 양식을 간소하지만 작성하면 DB에 저장되어 회원가입이 완료됨. 제출하면 완료형식이 나타나며, 로그인하기 버튼을 누르면 로그인

#### /dhkdneod/login 
로그인 페이지에서 회원가입한 아이디 패스워드를 입력하면 로그인되어 id 정보와 함께 환영합니다가 표시되며, 세션이 생성됨. 
비밀번호 변경 누를 시 비밀번호 변경 페이지로 이동
로그인된 화면에서 회원탈퇴시에 회원탈퇴를 하여 DB에서 회원삭제

#### /dhkdneod/select
select문을 이용하여 앞의 내용을 선택할시 뒤의 셀렉트가 달라지는 동적셀렉트 자바스크립트 실습

#### /intro/나온 학교/전공/나이(숫자)/상세소개
url에 입력한 대로 정보를 출력하는 실습

#### /novel/숫자(화수)/대상1/대상2
url에 입력한 대로 정보를 출력하는 실습. 기본값이 있어 입력하지 않고 /novel만 써도 기본값이 출력됨

#### /statictest
스테틱 파일로 이미지 서버에 저장하여 불러옴

#### /ajax
회원가입한 정보 로그인을 ajax 전송하여 페이지 변화없이 로그인을 확인하도록 실습

#### /fileupload
파일을 업로드하면 서버에 저장되는 실습

#### /checkbox
체크박스에서 선택한 모든 값들을 확인하는 실습

#### /toeicinput
공부일수와 성적 3개의 데이터를 입력하고 학습 시작을 하여, 결과에서 공부일수를 입력하면 그에 따라 선형회귀함수를 통해 인공지능 학습을 하여 점수결과를 보여줌
pytorch 모듈 사용으로 pytorch모듈 설치 필요
