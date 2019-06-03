(function(){

  //var fileType; //define global variable

  // mstr is a global object from mstrgdc-2.0.js, which represents the data connector framework

  var myConnector = mstr.createDataConnector();

  // Connector must define fetchTable function.

  myConnector.fetchTable = function(table, params, doneCallback) {

    // params represents the information sent by connector to MSTR at interactive phase

    var mstrObj = JSON.parse(params);

    var file = mstrObj.connectionData.file;

    var url = file;
	//var data = mstrObj.connectionData.data;
    // Retrieve file type from params

    //fileType = mstrObj.fileType;

    /*if(fileType == "EXCEL"){

      getFileBlob(url, function (fileObject) {

        var reader = new FileReader();

        reader.onload = function(event) {

          var contents = new Uint8Array(reader.result);

          var data = uintToString(contents);

          table.appendRawData(btoa(data));

          doneCallback(table);

        };

        reader.readAsArrayBuffer(fileObject);

      });

    }

    else{*/

      /*$.get(url, function(resp) {

        var data = resp;

        if (fileType == "JSON"){

          data = JSON.stringify(resp);

        }

        table.appendRawData(data);

        doneCallback(table);

      });*/
	  if(table.tableSchema.tableName == "TableA"){
		  var data = mstrObj.connectionData.tabA;
		  var det = JSON.stringify(data);
		  table.appendRawData(det);
	  }
		  
	  if(table.tableSchema.tableName == "TableB"){
		  var data = mstrObj.connectionData.tabB;
		  var det = JSON.stringify(data);
		  table.appendRawData(det);
	  }
	  
	
    doneCallback(table);

    //}

  };

  // validateDataConnector does the validation check of the connector

  mstr.validateDataConnector(myConnector);

  // Create event listeners for when the user submits the form

  $(document).ready(function() {

    $("#submitButton").click(function() {

      var content = $("#file").val();

      mstr.connectionName = "RawDataFiles";

      // connectionData is a JSON object. Connector can put any information here.

      mstr.connectionData = {};

      mstr.connectionData.file = content;
	  mstr.connectionData.tabA = [
  {
    "album": "The White Stripes",
    "year": 1999,
    "US_peak_chart_post": "3"
  },
  {
    "album": "De Stijl",
    "year": 2000,
    "US_peak_chart_post": "6"
  }
];
mstr.connectionData.tabB = [
  {
    "album": "The White Stripes",
    "year": 2099,
    "US_peak_chart_post": "14"
  },
  {
    "album": "De Stijl",
    "year": 2104,
    "US_peak_chart_post": "26"
  }
];
      // Get file type from extension

      fileType = content.split('.').pop().toUpperCase();

      /*if(fileType == "JSON"){

        mstr.fileType = "JSON";

      }*/
	  mstr.fileType = "JSON";

      /*else if(fileType == "XLS" || fileType == "XLSX" ){

        mstr.fileType = "EXCEL";

      }*/

      // MUST define tableList field. Can import multiple tables in one connection.

      mstr.tableList = [];

      mstr.tableList.push({tableName: "TableA",fileType:"JSON"});
	  mstr.tableList.push({tableName: "TableB",fileType:"JSON"})

      // Inform that interactive phase is finished and send information to MSTR.

      window.mstr.submit();

    });

  });

  // EXCEL reader helper functions

  /*function getFileBlob(url, cb) {

    var xhr = new XMLHttpRequest();

    xhr.open("GET", url);

    xhr.responseType = "blob";

    xhr.addEventListener('load', function() {

      cb(xhr.response);

    });

    xhr.send();

  };

  function uintToString(uintArray) {

    var out = "";

    var len, i;

    len = uintArray.length;

    for(i = 0; i < len; i++){

      c = uintArray[i];

      out += String.fromCharCode(c);

    }

    return out;

  }*/

})();