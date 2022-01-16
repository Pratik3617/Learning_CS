$(document).ready(function() {
    $.getJSON("/displayallCategoryjson", function(data) {
        $.each(data, function(index, item) {
            $("#cid").append($ ('<option>').text(item[1]).val(item[0]))
        })
    })

    $("#cid").change(function(){
         $("#sid").empty()
         $('#sid').append($('<option>').text('- Select Subject -'))
         $.getJSON("/displayallSubjectjson",{cid:$('#cid').val()},function(data){
                $.each(data,function(index,item){
                    $("#sid").append($('<option>').text(item[2]).val(item[1]))
                })
         })

    })

    $("#sid").change(function(){
         $("#coid").empty()
         $('#coid').append($('<option>').text('- Select Course -'))
         $.getJSON("/displayallCoursejson",{sid:$('#sid').val()},function(data){
                $.each(data,function(index,item){
                    $('#coid').append($('<option>').text(item[3]).val(item[2]))
                })
         })

    })


    $('#search').keyup(function(){
        $.getJSON('/searching',{search:$('#search').val()},function(data){
            let htm=''
            $.each(data,function(index,item){

                htm+="<a href='/coursePreview?row=("+item+")'>"
                               htm+="<div class='Box'>"
                                    htm+="<div><img src='/static/"+item[7]+"'></div>"
                                    htm+=`<div class="topic">
                                        ${item[3]}
                                    </div>
                                    <hr>
                                        <div class="adjust">
                                            <div>
                                                ${item[11]} Lectures
                                            </div>
                                            <div>
                                                <span><i class="far fa-clock"></i></span>&nbsp;&nbsp;${item[6]} hours
                                            </div>
                                        </div>
                                    <hr>
                                    <div>
                                        <span><i class="far fa-user"></i> </span>&nbsp;&nbsp;${item[9]}
                                    </div>
                                    <div>
                                        Rating:${item[5]} <span><i class="fas fa-star"></i></span>
                                    </div>
                                    <div>
                                        &#8377; ${item[10]} /-
                                    </div>
                                    <div>
                                        <button>BUY NOW</button>
                                    </div>
                                </div>
                            </a>`

            })
            $('#result').html(htm);
        })
    })



})



