
$(document).ready(function() {
    $('.languages').select2({
        minimumResultsForSearch: Infinity,
        containerCssClass: "error",
        dropdownCssClass: "test"
    });
});

Fancybox.bind(document.getElementById("comments_carousel"), "[data-fancybox]", {});