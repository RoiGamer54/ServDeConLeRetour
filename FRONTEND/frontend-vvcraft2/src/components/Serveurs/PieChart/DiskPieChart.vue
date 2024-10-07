<template>
  <div>
    <canvas ref="diskChart"></canvas>
  </div>
</template>

<script>
import { Chart, PieController, ArcElement, Tooltip, Legend } from 'chart.js';

export default {
  name: 'PieChartVue',
  props: ['data'],
  mounted() {
    this.renderChart();
  },
  watch: {
    data: 'renderChart'  // Re-render the chart when data changes
  },
  methods: {
    renderChart() {
      if (this.chart) {
        this.chart.destroy();
      }
      
      // Register the Pie controller and required elements
      Chart.register(PieController, ArcElement, Tooltip, Legend);

      const ctx = this.$refs.diskChart.getContext('2d');
      this.chart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: this.data.labels,
          datasets: [
            {
              label: 'Utilisation des Disques',
              backgroundColor: ['#FF6384', '#36A2EB'],
              data: this.data.datasets[0].data,
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
        }
      });
    }
  },
};
</script>

<style scoped>
  canvas {
  width: 100%;
  height: 400px;
  }
</style>
