var ingID = 0;

$(document).ready(function() {
    var ings = $("#id_recipe_ingredients").val();
    if(ings) {
        var container = $("#ing-container");
        ings = ings.split("|");
        for(var i = 0; i<ings.length; i++) {
            var ing = ings[i].split(":");
            if(ing[2] == "units") {
                ing[2] = "";
            }
            container.append("<div id='ing-"+ingID+"' class='form-group'>\n"
                + "<div class='input-group'>\n"
                + "<span class='input-group-addon' id='ing-name-"+ingID+"'>Name:</span>\n"
                + "<input type='text' class='form-control' aria-describedby='ing-name-"+ingID+"' required='required' value='"+ing[0]+"'>\n"
                + "<span class='input-group-addon' id='ing-num-"+ingID+"'>Amount:</span>\n"
                + "<input type='number' step='any' class='form-control' aria-describedby='ing-num-"+ingID+"' required='required' value='"+ing[1]+"'>\n"
                + "<span class='input-group-addon' id='ing-unit-"+ingID+"'>Units:</span>\n"
                + "<input type='text' class='form-control' placeholder='optional' aria-describedby='ing-unit-"+ingID+"' value='"+ing[2]+"'>\n"
                + "<span class='input-group-btn'>\n"
                + "<button id='ing-del-"+ingID+"' class='btn btn-default ing-del' type='button'>X</button>\n"
                + "</span>\n"
                + "</div>\n"
                + "</div>\n");

        }
        ingID++;
    }
    if($("#ing-container").children().length == 1 && $("#ing-container div.input-group").first().children().length == 7) {
        $(".ing-del").parent().remove();
    }
});

$(document).on('click', "#ing-add", function() {
    ingID++;
    $("#ing-container").append("<div id='ing-"+ingID+"' class='form-group'>\n"
        + "<div class='input-group'>\n"
        + "<span class='input-group-addon' id='ing-name-"+ingID+"'>Name:</span>\n"
        + "<input type='text' class='form-control' aria-describedby='ing-name-"+ingID+"' required='required'>\n"
        + "<span class='input-group-addon' id='ing-num-"+ingID+"'>Amount:</span>\n"
        + "<input type='number' step='any' class='form-control' aria-describedby='ing-num-"+ingID+"' required='required'>\n"
        + "<span class='input-group-addon' id='ing-unit-"+ingID+"'>Units:</span>\n"
        + "<input type='text' class='form-control' placeholder='optional' aria-describedby='ing-unit-"+ingID+"'>\n"
        + "<span class='input-group-btn'>\n"
        + "<button id='ing-del-"+ingID+"' class='btn btn-default ing-del' type='button'>X</button>\n"
        + "</span>\n"
        + "</div>\n"
        + "</div>\n");
    if($("#ing-container").children().length == 2 && $("#ing-container div.input-group").first().children().length == 6) {
        $("#ing-container div.input-group").first().append("<span class='input-group-btn'>\n"
            + "<button id='ing-del' class='btn btn-default ing-del' type='button'>X</button>\n"
            + "</span>\n");
    }
});

$(document).on('click', '.ing-del', function() {
   $(this).parent().parent().parent().remove();
    if($("#ing-container").children().length == 1 && $("#ing-container div.input-group").first().children().length == 7) {
        $(".ing-del").parent().remove();
    }
});

$(document).on('click', '#submit_recipe', function() {
    var text = $("#id_recipe_ingredients")
    text.val("");
    $("#ing-container div.input-group").each(function() {
        if (text.val() != "") {
            text.val(text.val() + "|");
        }
        var r = "";
        $(this).children("input").each(function() {
            if (r.length > 0 ) {
                r += ":";
            }
            r += $(this).val();
        });
        text.val(text.val() + r);
    });
});
