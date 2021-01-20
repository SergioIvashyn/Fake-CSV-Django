$(document).ready(function(){
    const arrayRangedFieldsValue = ['1', '3'];
    let columns = $(".column_id");
    let addButton = $(".add-row");
    let deleteButton = $(".delete-row");

    addButton.addClass('mt-2 btn btn-primary');
    $('#div_id_string_character, #div_id_column_separator, #div_id_name').removeClass('row');

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
    renderColumns();

    const handleColumnChange = function(){
        columns = $(".column_id");
        columns.unbind('change');
        columns.bind('change', function() {
            renderColumns();
        });
    };
    handleColumnChange();

    const renderLastFormSetElement = function(){
        deleteButton = $(".delete-row");

        $(deleteButton[deleteButton.length - 1]).on('click', function () {
            handleColumnChange();
        });
    };

    deleteButton.on('click', function () {
        handleColumnChange();
    });

    const renderLastInputs = function(){
        columns = $(".column_id");
        columnViewLogic(columns.length - 1, '');
    };

    renderLastInputs();

    addButton.on('click', function () {
        handleColumnChange();
        renderLastInputs();
        renderLastFormSetElement();
    });
});