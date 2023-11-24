$(document).ready(function() {
    $('.languages').select2({
        minimumResultsForSearch: Infinity,
        containerCssClass: "error",
        dropdownCssClass: "test"
    });
});

const commentsCarousel = document.getElementById("comments_carousel");

Fancybox.bind(commentsCarousel, "[data-fancybox]", {});
