Chart.defaults.global.animation.duration = 0;
Chart.defaults.global.defaultFontSize = 12;

var config = {
    "type": "gauge",
    "data": {
        "datasets": [
            {
                "data": [],
                "backgroundColor": [],
                "borderWidth": 0,
                "hoverBackgroundColor": [],
                "hoverBorderWidth": 0
            }
        ],
        "current": 135,
    },
    "options": {
        "panel": {
            "min": 0,
            "max": 100,
            "tickInterval": 1,
            "tickColor": "rgb(0, 0, 0)",
            "tickOuterRadius": 99,
            "tickInnerRadius": 95,
            "scales": [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            "scaleColor": "rgb(0, 0, 0)",
            "scaleBackgroundColor": "rgb(105, 125, 151)",
            "scaleTextRadius": 80,
            "scaleTextSize": 8,
            "scaleTextColor": "rgba(0, 0, 0, 1)",
            "scaleOuterRadius": 99,
            "scaleInnerRadius": 93,
        },
        "needle": {
            "lengthRadius": 100,
            "circleColor": "rgba(188, 188, 188, 1)",
            "color": "rgba(180, 0, 0, 0.8)",
            "circleRadius": 7,
            "width": 5,
        },
        "cutoutPercentage": 90,
        "rotation": (1 / 2 + 1 / 3) * Math.PI,
        "circumference": 2 * Math.PI * 2 / 3,
        "legend": {
            "display": false,
            "text": "legend"
        },
        "tooltips": {
            "enabled": false
        },
        "title": {
            "display": true,
            "text": "LEVEL OF ANONYMITY",
            "position": "bottom"
        },
        "animation": {
            "animateRotate": false,
            "animateScale": false
        },
        "hover": {
            "mode": null
        }
    }
};

window.onload = function () {
    var ctx = document.getElementById('chart').getContext('2d');
    window.chart = new Chart(ctx, config);
};

setTimeout(5000, function () {
    window.chart.update();
})