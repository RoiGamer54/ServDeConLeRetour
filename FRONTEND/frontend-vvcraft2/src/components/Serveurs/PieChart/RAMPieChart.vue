<template>
    <div>
      <canvas ref="ramChart"></canvas>
    </div>
  </template>
  
  <script>
  import { Chart, PieController, ArcElement, Tooltip, Legend } from 'chart.js';
  
  export default {
    name: 'RamPieChart',
    props: ['data'],
    mounted() {
      this.renderChart();
    },
    watch: {
      data: 'renderChart', 
    },
    methods: {
      renderChart() {
        if (this.chart) {
          this.chart.destroy();
        }
        Chart.register(PieController, ArcElement, Tooltip, Legend);
  
        const ctx = this.$refs.ramChart.getContext('2d');
        this.chart = new Chart(ctx, {
          type: 'pie',
          data: {
            labels: this.data.labels,
            datasets: [
              {
                label: 'Utilisation de la RAM',
                backgroundColor: ['#FF6384', '#36A2EB'],
                data: this.data.datasets[0].data,
              },
            ],
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
          },
        });
      },
    },
  };
  </script>
  
<style scoped>
    canvas {
      width: 100%;
      height: 400px;
    }
</style>