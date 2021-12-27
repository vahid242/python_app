import pandas
import justpy as jp

data = pandas.read_excel('Canada.xlsx')
share = data.groupby(['province']) ['area'].mean()
print(share)

# print(data.shape)
# print(data.columns)
# print(data.head())
#print(data['province'])

chart_def = """
{
    chart: {
        type: 'pie'
    },
    title: {
        text: ''
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Land and freshwater area, by province and territory', classes="text-h3 text-center q-pa-md")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc_data = [{"name":v1, "y":v2} for v1, v2 in zip(share.index, share)]
    hc.options.series[0].data = hc_data
    return(wp)

jp.justpy(app)
