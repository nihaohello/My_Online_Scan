 <script type="text/javascript">
    var url="";
    var ip="";
    var daochu="";
    var httpHeaders="/api/httpHeader";
    var traceRoutes="/api/traceRoute";
    add_res="";

function httpHeader(url){
    $("#t_body").html(JSON.stringify([{"url":url}]));
    $.post(httpHeaders,JSON.stringify([{"url":url}]),function (results){
        $("#result").html("获取中:")
        if(results){
            /*for(var i in results){
                add_res="<tr><td>"+results[i]+"</td></tr>"+add_res;
                daochu+=results[i]+"\r\n"
            }*/
            $("#t_body").html(results);
        }else{
            $("#t_body").html("没有结果或到了ip100上线");
        }
    },"json");
}

function Trace_Route(url){
    $("#t_body").html(JSON.stringify([{"url":url}]));
    $.post(traceRoutes,JSON.stringify([{"url":url}]),function (results){
        $("#result").html("获取中:")
        if(results){
            /*for(var i in results){
                add_res="<tr><td>"+results[i]+"</td></tr>"+add_res;
                daochu+=results[i]+"\r\n"
            }*/
            $("#t_body").html(results);
        }else{
            $("#t_body").html("没有结果或到了ip100上线");
        }
    },"json");
}


$(function() {
    $("#httpHeader").click(function() {
        $("#t_body").html("")
        var url=$("#url").val();
        if(urlcheck()){
            httpHeader(url);
        }
    });
    $("#Trace_Route").click(function() {
        $("#t_body").html("")
        var url=$("#url").val();
        if(urlcheck()){
            Trace_Route(url);
        }
    });
    $("#Whois_Information").click(function() {
        $("#t_body").html("")
        var url=$("#url").val();
        if(urlcheck()){
            request(url)
        }
    });
    $("#Website_on_the_same_server").click(function() {
        $("#t_body").html("")
        var url=$("#url").val();
        if(urlcheck()){
            request(url)
        }
    });
    $("#DNS_server_record").click(function() {
        $("#t_body").html("")
        var url=$("#url").val();
        if(urlcheck()){
            request(url)
        }
    });
    $("#Reverse_IP_Address").click(function() {
        $("#t_body").html("")
        var url=$("#url").val();
        if(urlcheck()){
            request(url)
        }
    });
    $("#Nmap_running_services").click(function() {
        $("#t_body").html("")
        var url=$("#url").val();
        if(urlcheck()){
            request(url)
        }
    });
    $("#Page_Links").click(function() {
        $("#t_body").html("")
        var url=$("#url").val();
        if(urlcheck()){
            request(url)
        }
    });

    $("#hackertartget_All").click(function() {
        $("#t_body").html("")
        var url=$("#url").val();
        if(urlcheck()){
            request(url)
        }
    });




    $("#download").click(function(){
        $('#download').attr("href","data:text/plain;base64,"+btoa(daochu))
    });
});



</script>