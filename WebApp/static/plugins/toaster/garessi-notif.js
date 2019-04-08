$("[data-content]").map(function(i) {
  var content = $(this).attr('data-content');
  var idnotif = $(this).attr('data-display');
  var filter = $(this).attr('data-placement');
  var filter = filter.split("-");


  if (filter[0] === "top") {
      var key = 0;
  var no = 0;
  var arr = [];
    $('[data-display="'+idnotif+'"]').click(function(){

      var placement = $(this).attr('data-placement');
      var s =  idnotif+no;
      var top = 10 * key * 5;

    if (arr !== '') {
      arr.push([s,top]);
        $('body').append('<div id="'+arr[key][0]+'" data-no="'+key+'" class="g-notif g-notif--'+placement+'" style="top:'+ arr[key][1] +'px;">'+content+' <span class="material-icons close-g-notif close-g-notif'+no+'">close</span></div>');
      }else{
        $('body').append('<div id="'+idnotif+'0" data-no="'+key+'" class="g-notif g-notif--'+placement+'" style="top:0px;">'+content+' <span class="material-icons close-g-notif close-g-notif'+no+'">close</span></div>');
      }
     var notifTime = setInterval(function () {
             $('#'+s).fadeOut(1000,function(){
            var now_key = $(this).attr('data-no');
              arr.splice(now_key,1);
              key -=1;
              var n = 0;
              for (var j =0; j < arr.length; j++) {
                $('#'+arr[j][0]).css({
                  "top": 10 * n * 5 +'px',
                  "transition":"0.3s"
                });
                $('#'+arr[j][0]).attr('data-no',j);
              n+=1;
              }
              $(this).remove();
            });
            clearInterval(notifTime);
          }, 3000);
      $('.close-g-notif'+no).on('click',function(){
        var now_key = $(this).parent().attr('data-no');
        arr.splice(now_key,1);
        key -=1;
        var n = 0;
        for (var j =0; j < arr.length; j++) {
          $('#'+arr[j][0]).css({
            "top": 10 * n * 5 +'px',
             "transition":"0.3s"
          });
          $('#'+arr[j][0]).attr('data-no',j);
        // console.log( 10 * n * 5 +'px');
        n+=1;
        }
        $(this).parent().remove();
          // console.log(arr);
      });

    no +=1;
    key +=1;
    });
  }
  if (filter[0] === "bottom") {
      var key = 0;
  var no = 0;
  var arr = [];
$('[data-display="'+idnotif+'"]').click(function(){

      var placement = $(this).attr('data-placement');
      var s =  idnotif+no;
      var bottom = 10 * key * 5;
    if (arr !== '') {
      arr.push([s,bottom]);
      $('body').append('<div id="'+arr[key][0]+'" data-no="'+key+'" class="g-notif g-notif--'+placement+'" style="bottom:'+ arr[key][1] +'px;">'+content+' <span class="material-icons close-g-notif close-g-notif'+no+'">close</span></div>');
      }else{
      $('body').append('<div id="idnotif0" data-no="'+key+'" class="g-notif g-notif--'+placement+'" style="bottom:0px;">'+content+' <span class="material-icons close-g-notif close-g-notif'+no+'">close</span></div>');
      }
     var notifTime = setInterval(function () {
             $('#'+s).fadeOut(1000,function(){
            var now_key = $(this).attr('data-no');
              arr.splice(now_key,1);
              key -=1;
              var n = 0;
              for (var j =0; j < arr.length; j++) {
                $('#'+arr[j][0]).css({
                  "bottom": 10 * n * 5 +'px',
                  "transition":"0.3s"
                });
                $('#'+arr[j][0]).attr('data-no',j);
              n+=1;
              }
              $(this).remove();
            });
            clearInterval(notifTime);
          }, 3000);
      $('.close-g-notif'+no).on('click',function(){
        var now_key = $(this).parent().attr('data-no');
        arr.splice(now_key,1);
        key -=1;
        var n = 0;
        for (var j =0; j < arr.length; j++) {
          $('#'+arr[j][0]).css({
            "bottom": 10 * n * 5 +'px',
             "transition":"0.3s"
          });
          $('#'+arr[j][0]).attr('data-no',j);
        // console.log( 10 * n * 5 +'px');
        n+=1;
        }
        $(this).parent().remove();
          // console.log(arr);
      });

    no +=1;
    key +=1;


    });

  }
}).get();
