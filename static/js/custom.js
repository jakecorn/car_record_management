$(function(){
    $('#color_filter').change(function(){
        var color = $(this).val();
        $.ajax({
            url: '/car/list',
            method: 'get',
            data: {'color': color},
            success:function(data){
                $('#car_list_table tbody').html(data)
                change_sequence();
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
    change_sequence();
});

function change_sequence(){
    var c = {};

    $("#car_list_table tbody tr").draggable({
            helper: "clone",
            start: function(event, ui) {
                c.tr = this;
                c.helper = ui.helper;
                console.log("start")
            }
    });

    $("#car_list_table tbody tr").droppable({
        drop: function(event, ui) {
            var moved_row = ui.draggable.clone();
            ui.draggable.detach();
            var moved_car_id = ui.draggable.attr("car-id");
            var last_car_id = $(this).attr("car-id");
            console.log(moved_car_id)
            console.log("moved_car_id"+ moved_car_id)
            console.log("drop_into"+ last_car_id)
            $(this).after(moved_row);
            $.ajax({
                url: '/car/update/order',
                method: 'get',
                data: {'last_car_id': last_car_id, 'id': moved_car_id},
                success:function(data){
                    alert("New sequence is saved.")
                    change_sequence()
                }
            })
            $(c.tr).detach();
            $(c.helper).detach();
        }
    });
}