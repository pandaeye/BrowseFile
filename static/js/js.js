var nCurrentIndex;

function clickSaveCookie(str) {
    var xmlhttp;
    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    }
    else {// code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function ()//返回处理函数
    {
    }

    //var sUrl = encodeURI("SaveCooie?q=" + str);
    var sUrl = "SaveCooie?q=" + encodeURIComponent(str);//str需要转码，因为包含汉字等。但是str可能包含+，#等字符，使用encodeURIComponent可以将+等编码，传输url时+不会被当成空格
    xmlhttp.open("GET", sUrl, true);
    xmlhttp.send();
}

function showfirst() {
    //��ʼֻ����3��ͼ start
    nCurrentIndex = 0;
    if (document.images[0]) {
        document.images[0].setAttribute("src", document.images[0].getAttribute("tmp"));
    }
    if (document.images[1]) {
        document.images[1].setAttribute("src", document.images[1].getAttribute("tmp"));
        nCurrentIndex = nCurrentIndex + 1;
    }
    if (document.images[2]) {
        document.images[2].setAttribute("src", document.images[2].getAttribute("tmp"));
        nCurrentIndex = nCurrentIndex + 1;
    }
    if (document.images[3]) {
        document.images[3].setAttribute("src", document.images[3].getAttribute("tmp"));
        nCurrentIndex = nCurrentIndex + 1;
    }
    if (document.images[4]) {
        document.images[4].setAttribute("src", document.images[4].getAttribute("tmp"));
        nCurrentIndex = nCurrentIndex + 1;
    }
    //��ʼֻ����3��ͼ end
}

window.onscroll = function () {
    docImg = document.images;
    if (docImg[nCurrentIndex - 1]) {
        if (docImg[nCurrentIndex - 1].getBoundingClientRect().top < 0)//����nCurrentIndex-1��ͼƬ���Ͻ������뿪����ʱ
        {
            if (docImg[nCurrentIndex + 1]) {
                docImg[nCurrentIndex + 1].setAttribute("src", docImg[nCurrentIndex + 1].getAttribute("tmp"));
                nCurrentIndex = nCurrentIndex + 1;
            }
            if (docImg[nCurrentIndex + 1]) {
                docImg[nCurrentIndex + 1].setAttribute("src", docImg[nCurrentIndex + 1].getAttribute("tmp"));
                nCurrentIndex = nCurrentIndex + 1;
            }
            if (docImg[nCurrentIndex + 1]) {
                docImg[nCurrentIndex + 1].setAttribute("src", docImg[nCurrentIndex + 1].getAttribute("tmp"));
                nCurrentIndex = nCurrentIndex + 1;
            }
        }
    }
}

function clickToMark() {
    var xmlhttp;
    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    }
    else {// code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function ()//���ش�����
    {
        document.getElementById("myDiv").innerHTML = xmlhttp.responseText;
    }
    var str = document.getElementById("bt").getAttribute("tmp");
    var sUrl = encodeURI("MarkDir?q=" + str);
    xmlhttp.open("GET", sUrl, true);
    xmlhttp.send();
}

function clickToPage(page) {
    var xmlhttp;
    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    }
    else {// code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function ()//���ش�����
    {
        document.getElementById("myDiv").innerHTML = xmlhttp.responseText;
        document.getElementById("CurrentPage").innerHTML = nCurrentPage;
    }
    var nCurrentPage = Number(document.getElementById("CurrentPage").innerHTML);
    var nPageNum = Number(document.getElementById("PageNum").innerHTML);
    nCurrentPage = nCurrentPage + page;
    nCurrentPage = Math.max(nCurrentPage,1);
    nCurrentPage = Math.min(nCurrentPage,nPageNum);
    var sUrl = encodeURI("OpenTxtPage?page=" + nCurrentPage);
    xmlhttp.open("GET", sUrl, true);
    xmlhttp.send();
}
