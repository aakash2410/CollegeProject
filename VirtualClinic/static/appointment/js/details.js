function getDate()
{
    today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //As January is 0.
    var yyyy = today.getFullYear();
    var sp="-";
    if(dd<10) dd='0'+dd;
    if(mm<10) mm='0'+mm;
    var ans=yyyy+sp+mm+sp+dd
    document.write(ans);
    console.log(ans);
    };
    document.getElementsById(d).setAttribute("min", getDate());