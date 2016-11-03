<script type="text/javascript">
function countDown(secs,elem){
    var element = document.getElementById(elem);
    element.innerHtml = "please wait for" + secs + "seconds";
    secs--;
    var timer = setTimeout('countDown('+secs+',"'+elem+'")',1000);
}

</script>
<div id="status">
</div>
<script type="text/javascript">countDown(20,"status")</script>
