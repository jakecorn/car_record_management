$(function(){
    $('#color_filter').change(function(){
        var color = $(this).val();
        $.ajax({
            url: '/car/list',
            method: 'get',
            data: {'color': color},
            success:function(data){
                $('#car_list_table tbody').html(data)
            }
        })
    });

    $('.delete_car').click(function(){
        var car_id = $(this).attr('car-id');
        var delete_link = $(this).attr('delete-link');
        console.log(delete_link)
        $('#delete_confirmation').modal('show');
        $('#delete_confirmation #delete_link').attr('href', delete_link);
    });
})