// "개설학기","과목","캠퍼스","교수명","평점","과제","조모임","학점비율","구분"
// OpenSemester: 2021-1, 2021-2
// Subject:
// Campus: 서울
// Professor:
// GPA: 0 ~ 5
// Homework: 3없음, 2보통, 1많음
// GroupMeeting:  3많음, 2보통, 1없음
// PerOfCredits: 3학점느님, 2비율채워줌, 1매우깐깐함
//-----------------------------------------------------------

let selectedPart = '';
let resultData;
let majorResultData;
function sel(e){
    selectedPart = e.value; // 해당 버튼의 구분 return
    if(selectedPart === "전공")
    {
        console.log("전공입니다");
        document.getElementById("majorcategorySelector").value = "Default..";
        majorRecommendList();
    }
    else
    {
        console.log(selectedPart);
        document.getElementById("categorySelector").value = "Default..";
        $("#tableset").empty();
        $.ajax({
                    url:'RecommendLectures/',
                    data : {"input" : selectedPart},
                    type : "GET",
                    dataType : "json",
                    success:function(result){

                            result.sort(function(a,b){
                                return b.gpa - a.gpa;
                            });
                            resultData = result;

                            var str = '';
                            $.each(result , function(i){
                                str +=  '<tr><td style="font-size: small">' + result[i].subjects +
                                        '</td><td style="font-size: small">' + result[i].opensemester +
                                        '</td><td style="font-size: small">' + result[i].professor +
                                        '</td><td style="font-size: small">' + result[i].gpa +
                                        '</td><td style="font-size: small">' + result[i].groupmeeting +
                                        '</td><td style="font-size: small">' + result[i].homework +
                                        '</td><td style="font-size: small">' + result[i].perofcredits +
                                        '</td></tr>';
                            });
                            $("#tableset").append(str);
                    }
            });
        const lecturelist = document.querySelector('.lec-wrapper');
        lecturelist.classList.add('open');

    }
}

function closeRecommendList() {
    const lecturelist = document.querySelector('.lec-wrapper');
    lecturelist.classList.remove('open');
    $("#tableset").empty();
}


function sortCategory() {
    var selectCategory = document.getElementById('categorySelector');
    // 선택한 category 추출
    var selectvalue = selectCategory.options[selectCategory.selectedIndex].value;
    selectvalue = selectvalue.toLowerCase();
    resultData.sort(function(a,b){
        return b.gpa - a.gpa;
    });

    if(selectvalue === "homework" || selectvalue === "groupmeeting")
    {
        resultData.sort(function(a,b){
            console.log(a[selectvalue] + b[selectvalue]);
            var val1 = 0;
            var val2 = 0;
            if(a[selectvalue] === "없음") val1 = 3;
            else if(a[selectvalue] === "보통") val1 = 2;
            else val1 = 1;
            if(b[selectvalue] === "없음") val2 = 3;
            else if(b[selectvalue] === "보통") val2 = 2;
            else val2 = 1;
            return val2-val1;
        });
    }
    else if(selectvalue === "perofcredits")
    {
        resultData.sort(function(a,b){
            var val1 = 0;
            var val2 = 0;
            if(a[selectvalue] === "학점느님") val1 = 3;
            else if(a[selectvalue] === "비율채워줌") val1 = 2;
            else val1 = 1;
            if(b[selectvalue] === "학점느님") val2 = 3;
            else if(b[selectvalue] === "비율채워줌") val2 = 2;
            else val2 = 1;
            return val2-val1;
        });

    }

    $("#tableset").empty();
    var str = '';

    $.each(resultData , function(i){
        str +=  '<tr><td style="font-size: small">' + resultData[i].subjects +
                '</td><td style="font-size: small">' + resultData[i].opensemester +
                '</td><td style="font-size: small">' + resultData[i].professor +
                '</td><td style="font-size: small">' + resultData[i].gpa +
                '</td><td style="font-size: small">' + resultData[i].groupmeeting +
                '</td><td style="font-size: small">' + resultData[i].homework +
                '</td><td style="font-size: small">' + resultData[i].perofcredits +
                '</td></tr>';
    });
    $("#tableset").append(str);

}



function majorRecommendList()
{
    $("#majortable").empty();
    $.ajax({
        url:'RecommendLectures/',
        data : {"input" : selectedPart},
        type : "GET",
        dataType : "json",
        success:function(result){
            majorResultData = result;
            result.sort(function(a,b){
                return b.gpa - a.gpa;
            });
            resultData = result;
            console.log(result[0]);
            var essentialStr = '';
            var selectiveStr = '';
            $.each(result , function(i){
                if(result[i].division === "전필")
                {
                    console.log("전필 추가 : " + result[i]);
                    essentialStr +=  '<tr><td style="font-size: small">' + result[i].subjects +
                            '</td><td style="font-size: small">' + result[i].opensemester +
                            '</td><td style="font-size: small">' + result[i].professor +
                            '</td><td style="font-size: small">' + result[i].gpa +
                            '</td><td style="font-size: small">' + result[i].groupmeeting +
                            '</td><td style="font-size: small">' + result[i].homework +
                            '</td><td style="font-size: small">' + result[i].perofcredits +
                            '</td><td style="font-size: small">' + result[i].class +
                            '</td><td style="font-size: small">' + result[i].division +
                            '</td></tr>';

                }
                else
                {
                    console.log("전선 추가 : " + result[i]);
                    selectiveStr +=  '<tr><td style="font-size: small">' + result[i].subjects +
                            '</td><td style="font-size: small">' + result[i].opensemester +
                            '</td><td style="font-size: small">' + result[i].professor +
                            '</td><td style="font-size: small">' + result[i].gpa +
                            '</td><td style="font-size: small">' + result[i].groupmeeting +
                            '</td><td style="font-size: small">' + result[i].homework +
                            '</td><td style="font-size: small">' + result[i].perofcredits +
                            '</td><td style="font-size: small">' + result[i].class +
                            '</td><td style="font-size: small">' + result[i].division +
                            '</td></tr>';
                }
            });
            $("#majortable").append(essentialStr + selectiveStr);
        }
    });

    const lecturelist = document.querySelector('.major-wrapper');
    lecturelist.classList.add('open');

}

function sortmajorCategory()
{
    var selectCategory = document.getElementById('majorcategorySelector');
    // 선택한 category 추출
    var selectvalue = selectCategory.options[selectCategory.selectedIndex].value;
    selectvalue = selectvalue.toLowerCase();

    $("#majortable").empty();

    resultData.sort(function(a,b){
        return b.gpa - a.gpa;
    });

    if(selectvalue === "homework" || selectvalue === "groupmeeting")
    {
        resultData.sort(function(a,b){
            console.log(a[selectvalue] + b[selectvalue]);
            var val1 = 0;
            var val2 = 0;
            if(a[selectvalue] === "없음") val1 = 3;
            else if(a[selectvalue] === "보통") val1 = 2;
            else val1 = 1;
            if(b[selectvalue] === "없음") val2 = 3;
            else if(b[selectvalue] === "보통") val2 = 2;
            else val2 = 1;
            return val2-val1;
        });
    }
    else if(selectvalue === "perofcredits")
    {
        resultData.sort(function(a,b){
            var val1 = 0;
            var val2 = 0;
            if(a[selectvalue] === "학점느님") val1 = 3;
            else if(a[selectvalue] === "비율채워줌") val1 = 2;
            else val1 = 1;
            if(b[selectvalue] === "학점느님") val2 = 3;
            else if(b[selectvalue] === "비율채워줌") val2 = 2;
            else val2 = 1;
            return val2-val1;
        });

    }
    var essentialStr = '';
    var selectiveStr = '';

    $.each(resultData , function(i){
        if(resultData[i].division === "전필")
        {
            essentialStr +=  '<tr><td style="font-size: small">' + resultData[i].subjects +
                    '</td><td style="font-size: small">' + resultData[i].opensemester +
                    '</td><td style="font-size: small">' + resultData[i].professor +
                    '</td><td style="font-size: small">' + resultData[i].gpa +
                    '</td><td style="font-size: small">' + resultData[i].groupmeeting +
                    '</td><td style="font-size: small">' + resultData[i].homework +
                    '</td><td style="font-size: small">' + resultData[i].perofcredits +
                    '</td><td style="font-size: small">' + resultData[i].class +
                    '</td><td style="font-size: small">' + resultData[i].division +
                    '</td></tr>';

        }
        else
        {
            selectiveStr +=  '<tr><td style="font-size: small">' + resultData[i].subjects +
                    '</td><td style="font-size: small">' + resultData[i].opensemester +
                    '</td><td style="font-size: small">' + resultData[i].professor +
                    '</td><td style="font-size: small">' + resultData[i].gpa +
                    '</td><td style="font-size: small">' + resultData[i].groupmeeting +
                    '</td><td style="font-size: small">' + resultData[i].homework +
                    '</td><td style="font-size: small">' + resultData[i].perofcredits +
                    '</td><td style="font-size: small">' + resultData[i].class +
                    '</td><td style="font-size: small">' + resultData[i].division +
                    '</td></tr>';
        }
    });
    $("#majortable").append(essentialStr + selectiveStr);
}



function closemajorRecommendList()
{
    const lecturelist = document.querySelector('.major-wrapper');
    lecturelist.classList.remove('open');
    $("#majortable").empty();

}