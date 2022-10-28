let countrySelect = $('#id_default_country').val();
if (!countrySelect) {
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function () {
    countrySelect = $(this).val();
    if (!countrySelect) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
})