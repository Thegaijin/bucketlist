$(document).ready(function() {
    $('a.account').on('click', function() {
        $('form').animate({ height: "toggle", opacity: "toggle" }, "slow");
    });
});