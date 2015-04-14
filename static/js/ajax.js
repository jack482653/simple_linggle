$(function() {
    $('a.button#btn_search').bind('click', function() {
      $.getJSON($SCRIPT_ROOT+'/search', {
        query: $('input[name="query"]').val(),
      }, function(data) {
        $('#query_result').remove();
        $('a#query').after('<div class="box container" id="query_result">\
                              <section>\
                                <table class="default">\
                                  <thead>\
                                    <tr>\
                                      <th>Result</th>\
                                      <th>Part of Speech</th>\
                                      <th>Count</th>\
                                    </tr>\
                                  </thead>\
                                  <tbody id="query_result_tdbody">\
                                  </tbody>\
                                </table>\
                              <section>\
                            </div>');
        for(var i in data.result) {
          for(var j in data.result[i]) {
            if(data.result[i][j][0] == "None") {
              data.result[i][j][0] = i
            }
            $('tbody#query_result_tdbody').append('<tr>\
                                                    <td>' + data.result[i][j][0] + '</td>\
                                                    <td>' + data.result[i][j][1] + '</td>\
                                                    <td>'+ data.result[i][j][2] +'</td>\
                                                  </tr>');
          }

        }
      });
      return false;
    });
});