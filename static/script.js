$(document).ready(function(){

  var attrs = { };

$.each($("p")[0].attributes, function(idx, attr) {
    attrs[attr.nodeName] = attr.nodeValue;
});


$("p").replaceWith(function () {
    return $("<div />", attrs).append($(this).contents());
});

$("div").addClass("form-group");
$("label").addClass("control-label col-sm-5");
$("input ").addClass("form-control col-sm-12");
});
