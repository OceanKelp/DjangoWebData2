
function abc() { 
    return ();
};


//map the data to the chart
function chartdata(jsonDatain) {
    // sessionStorage.setItem('chartData', JSON.stringify(jsonDatain));
    jsonDatain.forEach(entry => {
        entry.Date = new Date(entry.Date);


    });

    var xValues = jsonDatain.map(entry => entry.Date.toLocaleDateString());

    var openValues = jsonDatain.map(entry => entry.Open);
    var closeValues = jsonDatain.map(entry => entry.Close);
    var MA20Values = jsonDatain.map(entry => entry.MA20);
    var MA50Values = jsonDatain.map(entry => entry.MA50);
    var UpperBolValues = jsonDatain.map(entry => entry.UpperBol);
    var lowerBolValues = jsonDatain.map(entry => entry.LowerBol);
    var UpperminusPerValues = jsonDatain.map(entry => entry.UpperminusPer);
    var lowerPlusPerValues = jsonDatain.map(entry => entry.lowerPlusPer)

    //var difBolValues = jsonData2.map(entry => entry.difBol);
    //var CloseGtrupperValues = jsonData2.map(entry => entry.CloseGtrupper);
    //var CloseGtrPlusPerValues = jsonData2.map(entry => entry.CloseGtrPlusPer);
    //var CloseLowerLowerValues = jsonData2.map(entry => entry.CloseLowerLower);
    //var CloseLowerPlusPerValues = jsonData2.map(entry => entry.CloseLowerPlusPer);
    //var CloseMinusMA20Values = jsonData2.map(entry => entry.CloseMinusMA20);
    //var CloseMinusMA50Values = jsonData2.map(entry => entry.CloseMinusMA50);
    //var SMA20MinusMA50Values = jsonData2.map(entry => entry.SMA20MinusMA50)


    myChart = new Chart("ChartReal", {
        type: "line",
        data: {
            labels: xValues,
            datasets: [
                {
                    fill: false,        //fills in a bar chart
                    lineTension: 0,     // stright line
                    backgroundColor: "rgba(255,0,6,1)",   //color to fill in
                    borderColor: "rgba(0,0,7,1)",
                    data: openValues,
                    label: 'Open',
                    borderWidth: 3,
                    hidden: true,
                    pointRadius: 1
                },

                {
                    fill: false,        //fills in a bar chart
                    lineTension: 0,     // stright line
                    backgroundColor: "rgba(255,0,0,1)",   //color to fill in
                    borderColor: "rgba(0,0,0,1)",
                    data: closeValues,
                    label: 'Close',
                    borderWidth: 3,
                    pointRadius: 1
                },
                {
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "rgba(0,255,0,1)",
                    borderColor: "rgba(55,255,255,1)",
                    data: MA20Values,
                    label: 'MA20',
                    borderWidth: 2,
                    pointRadius: 1
                },
                {
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "rgba(255,20,255,1)",
                    borderColor: "rgba(55,205,200,1)",
                    data: MA50Values,
                    label: 'MA50',
                    borderWidth: 2,
                    pointRadius: 1,
                    borderDash: [5, 5]
                },
                {
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "rgba(0,0,255,1)",
                    borderColor: "rgba(0,0,255,1)",
                    data: UpperBolValues,
                    label: 'UpperBol',
                    borderWidth: 2,
                    pointRadius: 1
                },
                {
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "rgba(0,0,255,1)",
                    borderColor: "rgba(0,0,255,1)",
                    data: lowerBolValues,
                    label: 'lowerBol',
                    borderWidth: 2,
                    pointRadius: 1
                },
                {
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "rgba(0,0,255,1)",
                    borderColor: "rgba(0,255,0,1)",
                    data: UpperminusPerValues,
                    label: 'UpperminusPer',
                    borderWidth: 2,
                    pointRadius: 1
                },
                {
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "rgba(255,0,255,1)",
                    borderColor: "rgba(0,255,0,1)",
                    data: lowerPlusPerValues,
                    label: 'lowerPlusPer',
                    borderWidth: 2,
                    pointRadius: 1
                }
            ]
        },

        options: {
            //time: {
            //    unit: 'day',
            //    parser: 'YYYY-MM-DD'
            //},
            animation: false, // Disable animations
            legend: { display: true },
            scales: {
                yAxes: [{
                    type: 'logarithmic',
                    // type: 'linear',
                    gridLines: { display: true, color: "rgba(255, 255, 255,3 )" }
                }],
                xAxes: [{
                    gridLines: { display: true, color: "rgba(255, 255, 0, 1)" }
                }]
            }
        }

    });
};



//callback when a symbol is clicked
function CallBack(index, symbol) {

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; //get csrf token from hidden input
    fetch('plotreq', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }, //send back selected symbol
        body: JSON.stringify({ index: index, symbol: symbol }),
    })
        .then(response => response.json())
        .then(jd => {
            const jdj = JSON.parse(jd)  //parse the json string
            var lastDate = jdj[jdj.length - 1].Date;
            var userFriendlyDate = new Date(lastDate).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });

            var element = document.getElementById('stock');
            element.innerHTML = 'Chart of ' + symbol + '     last date ' + userFriendlyDate;


            updatechartJ(myChart, jdj);
        })

}


// update the chart with new data
function updatechartJ(chart, datain) {
    // get rid of old chart

    chart.destroy();
    chartdata(datain);
    chart.update();
}



</script >








//function createChart(chartid, chartData) {
//    console.log('data in', chartData);
//    console.log('Type of chartData:', typeof chartData);
//    console.log('Content of chartData:', chartData);

//    console.log('Before forEach loop:', chartData);
//    var dataArray = Object.values(chartData);

//    console.log('Before forEach loop:', dataArray);
   
//    dataArray.forEach(entry => {
//        entry.Date = new Date(entry.Date * 1000);
//    });

//    // dates
//    var xValues = dataArray.map(entry => entry.Date.toLocaleDateString());
//    var closeValues = dataArray.map(entry => entry.Close);
//    var MA20Values = dataArray.map(entry => entry.MA20);
//    var MA50Values = dataArray.map(entry => entry.MA50);
//    var UpperBolValues = dataArray.map(entry => entry.UpperBol);
//    var lowerBolValues = dataArray.map(entry => entry.LowerBol);
//    var UpperminusPerValues = dataArray.map(entry => entry.UpperminusPer);
//    var lowerPlusPerValues = dataArray.map(entry => entry.lowerPlusPer);

//    // Create a new Chart object
//    var newChart = new Chart(chartid, {
//        type: "line",
//        data: {
//            labels: xValues,
//            datasets: [
//                {
//                    fill: false,        //fills in a bar chart
//                    lineTension: 0,     // stright line
//                    backgroundColor: "rgba(255,0,0,1)",   //color to fill in
//                    borderColor: "rgba(0,0,0,1)",
//                    data: closeValues,
//                    label: 'Close',
//                    borderWidth: 3,
//                    pointRadius: 1
//                },
//                {
//                    fill: false,
//                    lineTension: 0,
//                    backgroundColor: "rgba(0,255,0,1)",
//                    borderColor: "rgba(55,255,255,1)",
//                    data: MA20Values,
//                    label: 'MA20',
//                    borderWidth: 2,
//                    pointRadius: 1
//                },
//                {
//                    fill: false,
//                    lineTension: 0,
//                    backgroundColor: "rgba(255,20,255,1)",
//                    borderColor: "rgba(55,205,200,1)",
//                    data: MA50Values,
//                    label: 'MA50',
//                    borderWidth: 2,
//                    pointRadius: 1,
//                    borderDash: [5, 5]
//                },
//                {
//                    fill: false,
//                    lineTension: 0,
//                    backgroundColor: "rgba(0,0,255,1)",
//                    borderColor: "rgba(0,0,255,1)",
//                    data: UpperBolValues,
//                    label: 'UpperBol',
//                    borderWidth: 2,
//                    pointRadius: 1
//                },
//                {
//                    fill: false,
//                    lineTension: 0,
//                    backgroundColor: "rgba(0,0,255,1)",
//                    borderColor: "rgba(0,0,255,1)",
//                    data: lowerBolValues,
//                    label: 'lowerBol',
//                    borderWidth: 2,
//                    pointRadius: 1
//                },
//                {
//                    fill: false,
//                    lineTension: 0,
//                    backgroundColor: "rgba(0,0,255,1)",
//                    borderColor: "rgba(0,255,0,1)",
//                    data: UpperminusPerValues,
//                    label: 'UpperminusPer',
//                    borderWidth: 2,
//                    pointRadius: 1
//                },
//                {
//                    fill: false,
//                    lineTension: 0,
//                    backgroundColor: "rgba(255,0,255,1)",
//                    borderColor: "rgba(0,255,0,1)",
//                    data: lowerPlusPerValues,
//                    label: 'lowerPlusPer',
//                    borderWidth: 2,
//                    pointRadius: 1
//                }
//            ]
//        },

//        options: {
//            // ... your options
//            legend: { display: true },
//            scales: {
//                yAxes: [{
//                    type: 'logarithmic',
//                    gridLines: { display: true, color: "rgba(0, 0, 0, 1)" }
//                }],
//                xAxes: [{
//                    gridLines: { display: true, color: "rgba(0, 0, 0, 1)" }
//                }]
//            }
//        }
//    });

//    return newChart;
//};


