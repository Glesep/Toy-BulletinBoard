var xhr

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            //var cookie = jQuery.trim(cookies[i]);
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function postData() {
    var D_title = document.getElementById('title').value;                                                             // username_ 값을 받아와 uname에 저장
    var D_contents = document.getElementById('contents').value;                                                               // userage_ 값을 받아와 uage에 저장

    var data = {title: D_title, contents: D_contents};                                                                         // 데이터를 딕셔너리 형태로 data 변수에 저장
    var jsondata = JSON.stringify(data);                                                                                 // JSON 형식으로 data를 변환, jsonstr 변수에 저장


    xhr = new XMLHttpRequest();                                                                                         // request 요청을 쉽게 할 수 있도록 객체 생성 (편지 준비)(AJAX 요청)
    xhr.onreadystatechange = function() {                                                                               // XMLHttpRequest 객체의 상태가 변경될 때마다 호출되는 이벤트 핸들러
        if (xhr.readyState == 4) {                                                                                      // 사용자가 응답을 처리할 수 있는 상태일 때,
            alert("게시글이 저장되었습니다.");
        }
    };
    xhr.open("POST", "/write", true);                                                                                   // /users 엔드포인트에 POST 명령 준비 (편지 작성)
    xhr.setRequestHeader("X-CSRFToken", csrftoken);                                                                     // X-CSRFToken에 csrftoken 값을 설정, CSRF 공격에 대한 예방
    xhr.setRequestHeader('Content-Type', 'application/json');                                                           // **JSON 파일 보낼 시 무조건 추가!!!!**
    xhr.send(jsondata);                                                                                                  // jsonstr 데이터 보내기 (편지 전송)
}