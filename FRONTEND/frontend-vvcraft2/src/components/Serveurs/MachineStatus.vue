<template>
  <div class="machine-info">
    <h3>Informations de la Machine</h3>

    <!-- Informations sur le Processeur -->
    <section v-if="!loading && systemInfo.cpu_info" class="core-section">
      <h4>Processeur</h4>
      <p><strong>Modèle:</strong> {{ systemInfo.cpu_info.model }}</p>
      <p><strong>Nombre de cœurs physiques:</strong> {{ systemInfo.cpu_info.cores }}</p>
      <p><strong>Nombre de cœurs logiques:</strong> {{ systemInfo.cpu_info.logical_cores }}</p>
      <p><strong>Utilisation totale:</strong> {{ systemInfo.cpu_info.total_usage }}%</p>
      
      <!-- Utilisation des cœurs avec des barres visuelles -->
      <div class="flex-boxing">
          <div class="core-usage" v-for="(usage, index) in systemInfo.cpu_info.usage_per_core" :key="index">
            <div class="w-75 core-info"> <!-- Ajout d'une classe pour la bordure et le padding -->
              <p>Cœur {{ index + 1 }}: {{ usage }}%</p>
              <div class="usage-bar">
                <div class="usage-bar-fill" :style="{ width: usage + '%' }"></div>
              </div>
            </div>
          
        </div>
      </div>
    </section>

    <!-- Conteneur principal avec disposition flex pour Processeur, OS et RAM -->
    <div class="machine-status">
      <!-- Informations sur l'OS -->
      <section v-if="!loading && systemInfo.os_info" class="status-section">
        <h4>OS</h4>
        <p><strong>Type:</strong> {{ systemInfo.os_info.os_type }}</p>
        <p><strong>Modèle de la machine:</strong> {{ systemInfo.os_info.machine_model }}</p>
        <p><strong>Nom de la machine:</strong> {{ systemInfo.os_info.node_name }}</p>
        <p><strong>Temps d'activité:</strong> {{ systemInfo.os_info.uptime.toFixed(2) }} heures</p>
      </section>

      <!-- Informations sur la RAM -->
      <section v-if="!loading && systemInfo.ram_info" class="status-section">
        <h4>RAM</h4>
        <p><strong>Capacité installée:</strong> {{ systemInfo.ram_info.total_installed.toFixed(2) }} Go</p>
        <p><strong>Utilisation:</strong> {{ systemInfo.ram_info.used.toFixed(2) }} Go / {{ systemInfo.ram_info.total_installed.toFixed(2) }} Go ({{ systemInfo.ram_info.percent_used }}%)</p>
        <!-- Camembert pour la RAM -->
        <RAMPieChart :data="formatRamChartData()" />
      </section>
    </div>

    <!-- Informations sur les disques dans un conteneur distinct -->
    <section v-if="!loading && systemInfo.disk_usage">
      <h4>Disques</h4>
      <div class="disk-container">
        <div v-for="(disk, diskName) in systemInfo.disk_usage" :key="diskName" class="disk-info">
          <h5>{{ diskName }}</h5>
          <p><strong>Capacité totale:</strong> {{ disk.total.toFixed(2) }} Go</p>
          <p><strong>Espace utilisé:</strong> {{ disk.used.toFixed(2) }} Go ({{ disk.percent }}%)</p>
          <p><strong>Espace libre:</strong> {{ disk.free.toFixed(2) }} Go</p>
          <!-- Camembert pour le disque -->
          <PieChartVue :data="formatChartData(disk)" />
        </div>
      </div>
    </section>

    <p v-else>Chargement des données...</p>
    <p v-if="error">{{ error }}</p>
  </div>
</template>


<script>
import axios from 'axios';
import PieChartVue from './PieChart/DiskPieChart.vue';
import RAMPieChart from './PieChart/RAMPieChart.vue';

export default {
  name: 'MachineInfo',
  components: {
    PieChartVue,
    RAMPieChart
  },
  data() {
    return {
      systemInfo: {},
      loading: true,
      error: '',
    };
  },
  mounted() {
    this.fetchMachineInfo();
  },
  methods: {
    async fetchMachineInfo() {
      try {
        const response = await axios.get('http://localhost:8000/api/machine/status/');
        this.systemInfo = response.data;
      } catch (err) {
        this.error = 'Erreur lors de la récupération des données.';
      } finally {
        this.loading = false;
      }
    },
    formatChartData(disk) {
      return {
        labels: ['Espace Utilisé', 'Espace Libre'],
        datasets: [
          {
            label: `Utilisation de ${disk.total.toFixed(2)} Go`,
            backgroundColor: ['#FF6384', '#36A2EB'],
            data: [disk.used.toFixed(2), disk.free.toFixed(2)],
          }
        ]
      };
    },
    formatRamChartData() {
      return {
        labels: ['Espace Utilisé', 'Espace Libre'],
        datasets: [
          {
            label: 'Utilisation de la RAM',
            backgroundColor: ['#FF6384', '#36A2EB'],
            data: [
              this.systemInfo.ram_info.used.toFixed(2),
              this.systemInfo.ram_info.total_installed.toFixed(2) -
                this.systemInfo.ram_info.used.toFixed(2),
            ],
          },
        ],
      };
    },
  },
};
</script>

<style scoped>
.machine-info {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
}

.flex-boxing {
  display: flex; 
  flex-wrap: wrap; 
  gap: 10px; 
  justify-content: center; /* Centre les cœurs */
}

.machine-status {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.status-section {
  width: 50%;
  padding: 10px;
}

.core-section {
  width: 75%; 
  margin: 0 auto; 
  padding: 10px;
}

.core-usage {
  flex: 1 1 30%; 
  width: 75%;
  margin-bottom: 10px;
  border: 1px solid #ccc; /* Couleur de la bordure */
  border-radius: 16px; 
  background-color: #333; 
}

.core-info {
  padding: 10px; 
  margin-bottom: 10px; 
  background-color: #f9f9f9; /* Même couleur que la bordure pour éviter le blanc */
}

.usage-bar {
  background-color: #f0f0f0;
  border-radius: 5px;
  overflow: hidden;
  height: 10px;
  width: 100%;
}

.usage-bar-fill {
  background-color: #007bff;
  height: 100%;
  transition: width 0.3s ease;
}

.disk-container {
  display: flex;
  flex-wrap: wrap;
}

.disk-info {
  width: 100%;
  max-width: 400px;
  margin: 10px;
}

canvas {
  max-width: 300px;
  margin: 20px auto;
}
</style>


