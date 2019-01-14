const chart2 = document.querySelector("#container2")
const data2 = JSON.parse(chart2.dataset.chart)

const teams = Object.entries(data2.matches_data).map(element => {
    return [element[0], concateObject(element[1])]
})
let values = teams.map(row => {
    return Object.keys(row[1])
});

let setOfTeams = [...new Set(values.reduce((a,b) => a.concat(b), []).filter(team => team !== ""))]
let teamsObject  = teams.map(row => row[1])
let totalWinsOfEachTeam = getEachTeamsWin(setOfTeams,teamsObject);

Highcharts.chart('container2', {
    chart: {
      type: 'column'
    },
    title: {
      text: data2.title
    },
    xAxis: {
      categories: teams.map(row => row[0])
    },
    yAxis: {
      min: 0,
      title: {
        text: data2.text
      },
      stackLabels: {
        enabled: true,
        style: {
          fontWeight: 'bold',
          color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
        }
      }
    },
    legend: {
      align: 'right',
      x: -30,
      verticalAlign: 'top',
      y: 25,
      floating: true,
      backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
      borderColor: '#CCC',
      borderWidth: 1,
      shadow: false
    },
    tooltip: {
      headerFormat: '<b>{point.x}</b><br/>',
      pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
    },
    plotOptions: {
      column: {
        stacking: 'normal',
        dataLabels: {
          enabled: true,
          color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white'
        }
      }
    },
    series: totalWinsOfEachTeam
  });  

function concateObject(arr){
    let obj = {}
    arr.forEach((el) => {
        obj[el.team] = el.total_wins
    })
    return obj
}

function teamsDataInAYear(arr){
    let years = [...new Set(arr.map(row => row.season))]
    let teamData = {}
    years.forEach(year => {
        arr.forEach(row => {
            if(row.season === year){
                if(teamData[row.season] === undefined){
                    teamData[row.season] = [row]
                }else{
                    teamData[row.season].push(row)
                }
            }
        })
    })
    return teamData;
}

function getEachTeamsWin(arr1,arr2){
    let winsOfEachTeam = {}
    arr1.forEach(team => {
        arr2.forEach(object => {
            if(team in object){
                if(winsOfEachTeam[team] === undefined){
                    winsOfEachTeam[team] = [object[team]]
                }else{
                    winsOfEachTeam[team].push(object[team])
                }
            }else{
                if(winsOfEachTeam[team] === undefined){
                    winsOfEachTeam[team] = [0]
                }else{
                    winsOfEachTeam[team].push(0)
                }
            }
        })
    })
    winsOfEachTeam = Object.entries(winsOfEachTeam).map(row => ({name:row[0], data:row[1]}))
    return winsOfEachTeam;
}
