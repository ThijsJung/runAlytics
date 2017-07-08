google.charts.load('current', {packages: ['corechart', 'line']});

// Callback function
function callAPI(url, cFunction) {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (xhttp.readyState == 4 && xhttp.status == 200) {
			cFunction(xhttp.responseText);
		}
	};
	xhttp.open("GET", url, true);
	xhttp.send();
}

// Call API 
function loadRouteData(run_id = 1){
	// console.log("Run ID: " + run_id);
	var url = 'runalytics/api/v1.0/runs/' + run_id + '/coordinates';
	callAPI(url, function(response){
		var myRouteData = JSON.parse(response);

		var polygon = L.polygon(myRouteData, {color : 'red'}).addTo(mymap);
		mymap.fitBounds(polygon.getBounds());
		// .bindPopup("Look what you ran!");
	})
}

function loadRunMenu(){
    // var url = 'runalytics/api/v1.0/runs';
    // var url = 'https://fmp7y4ey29.execute-api.eu-west-1.amazonaws.com/Prod/run';
	// callAPI(url , function(response){
    //     console.log(response)
		// var myRuns = JSON.parse(response);
    var myRuns = ["2015-12-13T15:06:22", "2015-12-24T10:59:57", "2015-12-06T14:37:21"];
    var selectRun = document.getElementById("user_run");
    
    for (var i = 0; i < myRuns.length; i++) {
        var runId = myRuns[i].id;
        var runName = myRuns[i].name;
        if (runName === null){
            runName = "Unnamed run " + runId;
        }
        var el = document.createElement("option");
        el.textContent = runName;
        el.value = runId;
        selectRun.appendChild(el);
    }
	// })
}

function loadPaceChart(runId){
    runId = 1;
    var url = '/runalytics/api/v1.0/runs/' + runId + '/pace';
    callAPI(url, function(response){
        var paceData = JSON.parse(response);
        var data = new google.visualization.DataTable(paceData);
        data.addColumn('string', 'X');
        data.addColumn('number', 'Pace');

        data.addRows(paceData);

        var options = {
            'title' : 'Pace (min/km)',
            hAxis: {
              title: 'Distance (km)',
              type: 'string'
            },
            vAxis: {
              title: 'Pace (min/km)'
            }
        };

        var chart = new google.visualization.ColumnChart(document.getElementById('pace_chart'));

        chart.draw(data, options);
    });
}

function loadHeartRateChart(runId){
    runId = 1;
    var url = '/runalytics/api/v1.0/runs/' + runId + '/heartrate';
    // console.log(url);
    callAPI(url, function(response){
        var heartRateData = JSON.parse(response);
        // console.log(heartRateData);
        var data = new google.visualization.DataTable();
        data.addColumn('number', 'X');
        data.addColumn('number', 'Heart rate');

        data.addRows(heartRateData);
        var options = {
            'title' : 'Heart rate (bpm)',
            hAxis: {
              title: 'Time (seconds)'
            },
            vAxis: {
              title: 'Heart rate (bpm)'
            }
        };

        var chart = new google.visualization.LineChart(document.getElementById('heart_rate_chart'));
        chart.draw(data, options);
    })
}

loadRunMenu();
// google.charts.setOnLoadCallback(loadPaceChart);
// google.charts.setOnLoadCallback(loadHeartRateChart);
