jQuery(function($){
    
    $('#edit').click(function() {
        $('.select').css('display','inline-block');
        $('#submit').css('display','inline-block');
        $('#cancel').css('display','inline-block');
    });

    $('#cancel').click(function() {
        $('.select').css('display','none');
        $('#submit').css('display','none');
        $('#cancel').css('display','none');
    });

});