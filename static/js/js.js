var nCurrentIndex;

function contains(arr, obj)
{  
    var i = arr.length;  
    while (i--) {  
        if (arr[i] === obj) {  
            return true;  
        }  
    }  
    return false;  
}  

function clickSaveCookie(str)
{

	var Days = 1; //�� cookie �������� 30 ��
	var exp  = new Date();    //new Date("December 31, 9998");
  	exp.setTime(exp.getTime() + Days*24*60*60*1000);

	var dicCookie=document.cookie.split(";");
	var sReadedStr = "";
	var bHaveCookie = false;
	for(var i=0;i<dicCookie.length;i++)
	{
		var c=dicCookie[i].trim();
		if(c.indexOf("Readed")==0)//ȡ���Ѷ����б�cookie
		{
				sReadedStr=c.split("=")[1];
				bHaveCookie = true;
				break;
		}
	}
	if(bHaveCookie == false)//û��Readed���cookieʱ�½�һ��
	{
			document.cookie= "Readed="+ str + "_" + ";expires=" + exp.toGMTString();
	}
	else
	{

		var sReadedList = sReadedStr.split("_");//δ���ڸ�����¼��ӽ�ȥ����_�ָ�
    if(!contains(sReadedList, str))
    {
        sReadedStr = sReadedStr + str + "_";
		document.cookie= "Readed="+ sReadedStr + ";expires=" + exp.toGMTString();
    }
  }
	return true;
}

function ShowTxt()
{
}

function showfirst()
{
	//���Ѿ������ļ�¼�һ�start
	var dicCookie=document.cookie.split(";");
	var str="";
	for(var i=0;i<dicCookie.length;i++)//��ȡ������¼�ַ���
	{
		var c=dicCookie[i].trim();
		if(c.indexOf("Readed")==0)
		{
			str=c.split("=")[1];
			break;
		}
	}
	var sReadedList = str.split("_");
	for(var i=0;i<sReadedList.length;i++)//��������¼�һ�
	{
		var c=sReadedList[i].trim();
		var o=document.getElementsByName(c);
		if(o.length==1)
		{
			o[0].setAttribute("style","width:500px;height:100px;background-color:#FF0000");
		}
	}
	//���Ѿ������ļ�¼�һ�end
	//��ʼֻ����3��ͼ start
	nCurrentIndex=0;
	if(document.images[0])
	{ 
			document.images[0].setAttribute("src",document.images[0].getAttribute("tmp"));
	}
	if(document.images[1])
	{ 
			document.images[1].setAttribute("src",document.images[1].getAttribute("tmp"));
			nCurrentIndex=nCurrentIndex+1;
	}
	if(document.images[2])
	{ 
			document.images[2].setAttribute("src",document.images[2].getAttribute("tmp"));
			nCurrentIndex=nCurrentIndex+1;
	}
	//��ʼֻ����3��ͼ end
}
window.onscroll = function ()
{
		/*var offsetPage = window.pageYOffset ? window.pageYOffset : window.document.documentElement.scrollTop,
		offsetWindow = offsetPage + Number(window.innerHeight ? window.innerHeight : document.documentElement.clientHeight),
		docImg = document.images,
		_len = docImg.length;
		if (!_len) return false;
		for (var i = 0; i < _len; i++) 
		{
			var attrSrc = docImg[i].getAttribute("tmp"),
				o = docImg[i], tag = o.nodeName.toLowerCase();
			if (o) 
			{
				postPage = o.getBoundingClientRect().top + window.document.documentElement.scrollTop + window.document.body.scrollTop; 
				if ((postPage > offsetPage && postPage < offsetWindow) ) 
				{
				    if (tag === "img" && attrSrc !== null) 
				    {
				        o.setAttribute("src", attrSrc);
				    }
				    o = null;
				}
			}
		};*/
		docImg = document.images;
		if(docImg[nCurrentIndex-1])
		{
				if(docImg[nCurrentIndex-1].getBoundingClientRect().top<0)//����nCurrentIndex-1��ͼƬ���Ͻ������뿪����ʱ
				{
						if(docImg[nCurrentIndex+1])
						{
							docImg[nCurrentIndex+1].setAttribute("src",docImg[nCurrentIndex+1].getAttribute("tmp"));
							nCurrentIndex=nCurrentIndex+1;
						}
						if(docImg[nCurrentIndex+1])
						{
							docImg[nCurrentIndex+1].setAttribute("src",docImg[nCurrentIndex+1].getAttribute("tmp"));
							nCurrentIndex=nCurrentIndex+1;
						}
						if(docImg[nCurrentIndex+1])
						{
							docImg[nCurrentIndex+1].setAttribute("src",docImg[nCurrentIndex+1].getAttribute("tmp"));
							nCurrentIndex=nCurrentIndex+1;
						}
				}
		}
}

function clickToMark()
{
		var xmlhttp;
		if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
		else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
		xmlhttp.onreadystatechange=function()//���ش�����
	  {
				document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
	  }
	  var str=document.getElementById("bt").getAttribute("tmp");
	  var sUrl=encodeURI("MarkDir?q="+str);
		xmlhttp.open("GET",sUrl,true);
		xmlhttp.send();
}

function clickToPage(page)
{
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
	var sUrl = encodeURI("OpenTxtPage?page="+page);
	xmlhttp.open("GET", sUrl, true);
	xmlhttp.send();
}
