function startjs(){
    dtpicker();
}


function dtpicker(){
    $(function () {
        $(".dates").datetimepicker({
            format: 'd.m.Y',
        });
    });
}


function showermenu() {

    var body_width = document.body.clientWidth

    // alert(body_width);
    
    if(body_width > 1000) {
        var wid = document.getElementById('leftbar').offsetWidth;
        var el = document.getElementById('leftbar').getElementsByClassName('txt');
        var tran = document.getElementsByClassName('level');
        if(wid > 60) {
            document.getElementById('leftbar').style.width = '60px';
            for(var i = 0; i < el.length; i += 1){
                el[i].style.display = 'none';
            }
            for(var j = 0; j < tran.length; j += 1){
                tran[j].style.padding = '0 0 0 60px';
            }
        } else {
            document.getElementById('leftbar').style.width = '200px';
            for(var i = 0; i < el.length; i += 1){
                el[i].style.display = 'block';
            }
            for(var j = 0; j < tran.length; j += 1){
                tran[j].style.padding = '0 0 0 200px';
            }
        }
    }

    if(body_width <= 1000) {
        // alert(body_width);
        var position_leftbat = document.getElementById('leftbar').offsetLeft;

        
        
        
        // $("html").css({'position':'absolute'});
        // $("html").css({'overflow-y':'hidden'});


        // alert(position_leftbat);
        if(position_leftbat < 0) {
            document.getElementById('leftbar').style.left = '0';
            document.getElementById('boxshadow').style.width = '100%';
            document.getElementById('boxshadow').style.height = '100%';
            document.body.style.position = 'fixed'
        } else {
            document.getElementById('leftbar').style.left = '-200px';
            document.getElementById('boxshadow').style.width = '0';
            document.getElementById('boxshadow').style.height = '0';
            document.body.style.position = 'relative'
        }

    }

}


function show_deleted_image(id) {
    if(document.getElementById('dele_'+id).checked) {
        document.getElementById('prev_'+id).style.opacity = 0.3
    }
    else {
        document.getElementById('prev_'+id).style.opacity = 1
    }
}


function show_loaded_image(id){
    console.log('id:'+id);
    let inpa = document.getElementById('uplo_'+id)
    inpa.addEventListener('change', function(e) {
        fileurl = window.URL.createObjectURL(e.target.files[0]);
        console.log('src:'+fileurl);
        document.getElementById('prev_'+id).style.backgroundImage = 'url('+fileurl+')';
        document.querySelector('.first').style.opacity = '1';
    })
}

















// function show_loaded_image(id){

//     console.log(id)
//     console.log(document.getElementById(id).checked);
//     document.getElementById('img_'+id).style.backgroundImage = 'none';


//     document.getElementById(id).addEventListener('input', function(e) {
        
//         console.log('changes have taken place')

//         var file = e.target.files[0];
//         console.log(file)

//         var reader = new FileReader();
//         reader.readAsDataURL(file);
//         console.log(reader)

        // reader.readAsDataURL(file);
        // var currentImageData = upload.target.result;
        // console.log(currentImageData)

    // })

// }



        



// function show_loaded_image(id){

//     console.log(id)
//     console.log(document.getElementById(id).checked);
//     document.getElementById('img_'+id).style.backgroundImage = 'none';

//     document.getElementById(id).addEventListener('input', function(e) {
//         var file = e.target.files[0];
//         console.log(file);
//         var reader = new FileReader();
//         reader.readAsDataURL(file);
//         reader.onloadend = function(upload) {
//             var currentImageData = upload.target.result;
//             console.log(currentImageData);
//             document.getElementById('img_'+id).style.backgroundImage = 'url('+currentImageData+')';
//             document.querySelector('.ncfi .empt .buttons .dele').style.display = 'block';
//         }
//     }); 
// }
















