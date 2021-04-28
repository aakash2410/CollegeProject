var users=[{
    name: 'Dr. Rajendra Sharma',
    specialisation: 'General Physician'
},
{
    name: 'Dr. Varija Verma',
    specialisation:'Gynaecologist'
},
];

window.addEventListener('load',function(){
    var results=document.getElementById('results');
    function search(){
        //get doctor
        var docField=document.getElementById('search');
        var doc=docField.value;
        console.log(doc);
        var res='';
        len=users.length;
        for(var i=0;i<len;i++){
                //check doctor
                if(hobby=='' || hobby==users[i].hobby){
                    res+='<div class="container">\
                    <div class="row">\
                    <div class="col-12 mt-3">\
                    <div class="card">\
                    <div class="card-horizontal">\
                    <div class="card-body">\
                    <h4 class="card-title">'+users[i].name+'</h4>\
                    <p class="card-text">'+users[i].specialisation+'</h4>\
                    </div></div></div></div></div></div></div>';
                }
        }
        results.innerHTML=res;
    }
        var y=document.getElementById('searchBtn');
        y.addEventListener('click',search);
});