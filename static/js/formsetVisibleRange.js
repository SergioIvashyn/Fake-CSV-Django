$(document).ready(function(){
    const arrayRangedFieldsValue = ['1', '3'];
    let columns = $(".column_id");
    const columnViewLogic = function (id, value) {
        let rangeMin = $(`#div_id_schemacolumn_set-${id}-range_min`);
        let rangeMax = $(`#div_id_schemacolumn_set-${id}-range_max`);
        if(arrayRangedFieldsValue.includes(('' + value))){
            rangeMin.show();
            rangeMax.show();
        }
        else{
            rangeMin.hide();
            rangeMax.hide();
        }
    };

    const renderColumns = function(){
        columns.each(function (index, value) {
            columnViewLogic($(value).attr('id').split('-')[1], $(value).val());
        });
    };

    const renderLastInputs = function(){
        let orders = $(".order");
        let rangesMin = $(".range_min");
        let rangesMax = $(".range_max");
        $(orders[orders.length - 1]).val(columns.length - 1);
        $(rangesMin[rangesMin.length - 1]).val(0);
        $(rangesMax[rangesMax.length - 1]).val(0);
    };

    const handleColumnChange = function(){
        columns = $(".column_id");
        columns.unbind('change');
        columns.bind('change', function() {
            renderColumns();
        });
    };

    handleColumnChange();
    renderLastInputs();

    renderColumns();
    $(".add-row").on('click', function () {
        handleColumnChange();
        renderLastInputs();
    });

    $(".delete-row").on('click', function () {
        handleColumnChange();
    });
});