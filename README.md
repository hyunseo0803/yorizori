## _DATABASES_
1. member_info
: id .Fk (아이디), password(비밀번호), email(이메일)
2. recipe
: id .Fk (아이디), source(재료), recipe_id .PK(레시피아이디), title(제목), info(소개), ex(설명), url(페이지링크), c_like(좋아요수)
3. review
: num .PK(일련번호), recipe_id .FK(레시피아이디), id .Fk (아이디), coment(댓글내용) 
4. manage
: id .Fk.PK (아이디), report(신고사유), c_report(신고횟수)

* 웹 자체 업로드일때, 아이디 = 회원식별 아이디
* 크롤링 업로드일때, 아이디= admin 
<br>

#### - 재료 input 컴포넌트 사용 변수
-	s1,s2,s3,s4 
(총 4개까지 주재료 입력 가능) 

<br>
<br>

## _DB예시 및 기능_ 

- 회원가입
Create id, password, email value (‘’,’’,’’)
#member_info테이블에 생성 
<br>
- 회원정보 수정
Update set id=’’ , password=’’, email=’’ where id=session.id
#현재 로그인 회원 정보 수정, member_info 테이블
<br>
- 회원 작업 공간
Select title from recipe where id=session.id
#현재 로그인 회원 아이디인 레시피 제목 가져오기, recipe 테이블 사용
<br>
- 업로드 기능
s=[]   <p># 리스트 생성, 재료 입력시, 리스트에 넣기 
For i in s: 
  if  i==null:
…..
  break
  
#for문 i가 null값이 될 때까지 
create 쿼리문 반복(이때, 재료1, 재료2, ... 재료만 다른 값 들어감)
recipe 테이블 사용 
이미지 업로드는 DB사용 X, 코드 폴더에 저장 
<br>
- 검색 기능
사용자가 감자, 김치 선택! 감자와 김치가 재료로 설정된
레시피를 찾아라(url). 좋아요 내림차순으로(desc). => 검색 결과 리스트 
1. recipe테이블의 재료중에서 감자 찾기 -> 
select recipe_id from recipe 
where sorce="감자" 
2. recipe테이블의 재료 중에서 김치 찾기 ->
select recipe_id from recipe 
where sorce="김치" 

==> select url from recipe 
where sorce='김치' and sorce='감자'
order by c_like desc; 
---->>> class 안에 list로 url 정렬 
<br>
- 게시물
1. 신고 컴포넌트 
#신고 사유 작성 후 확인버튼
-> manage 테이블의 report칼럼에 추가 
-> manage 테이블의 c_report 1씩 증가 
(이때, 게시물올린 회원 아이디값, 신고사유 받아옴)

2. 리뷰 컴포넌트_ 댓글달기 버튼
#review테이블에 현재 로그인 회원 아이디, 리뷰내용 추가 
3. 좋아요 컴포넌트 
#누르면 c_like 1씩 증가 
#두번 누르면 취소
<br>
- 관리자화면
#id=yorizori , password=1234, email=1234@naver.com 
#select member_info.id, manage.report, manage.c_report 리스트로 화면 출력 
#회원탈퇴 컴포넌트-> member_info에서 delete 
