var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: skills_list,
        datasets: [{
            label: 'Number of Occurrences',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: skills_values
        }]
    },

    // Configuration options go here
    options: {
                layout: {
                            padding: {
                                left: 30,
                                right: 30,
                                top: 30,
                                bottom: 30
                            }
                        }
    }
});