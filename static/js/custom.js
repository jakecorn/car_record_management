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
    change_sequence();
});

function delete_car(element){
    var car_id = $(element).attr('car-id');
    var delete_link = $(element).attr('delete-link');
    console.log(delete_link)
    $('#delete_confirmation').modal('show');
    $('#delete_confirmation #delete_link').attr('href', delete_link);
}

function change_sequence(){
    var c = {};
    $("#car_list_table tbody tr").draggable({
            helper: "clone",
            start: function(event, ui) {
                c.tr = this;
                c.helper = ui.helper;
            }
    });

    $("#car_list_table tbody tr").droppable({
        drop: function(event, ui) {
            var moved_row = ui.draggable.clone();
            ui.draggable.detach();
            var moved_car_id = ui.draggable.attr("car-id");
            var based_car_id = $(this).attr("car-id");
            $(this).after(moved_row);
            $.ajax({
                url: '/car/update/order',
                method: 'get',
                data: {'based_car_id': based_car_id, 'moved_car_id': moved_car_id},
                success:function(data){
                    $('#color_filter').change()
                }
            })
            $(c.tr).detach();
            $(c.helper).detach();
        }
    });
}