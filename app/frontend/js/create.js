var main = function() {
    $('a.account').click(function() {
        $('form').animate({ height: "toggle", opacity: "toggle" }, "slow");
    });
}
$(document).ready(main);