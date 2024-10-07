<template>
  <div class="serveurs-page">
    <!-- Onglets en haut de la page -->
    <ul class="tabs-onglet">
      <label
        class="tab"
        :class="{ active: activeTab === 'machineStatus' }"
        @click="setActiveTab('machineStatus')"
      >
        Etat de santé de la machine
      </label>
      <label
        class="tab"
        :class="{ active: activeTab === 'serviceStatus' }"
        @click="setActiveTab('serviceStatus')"
      >
        Information sur le service
      </label>
    </ul>

    <!-- Composants basés sur l'onglet sélectionné -->
    <MachineStatus v-if="activeTab === 'machineStatus'" />
    <OtherInfo v-if="activeTab === 'serviceStatus'" />
  </div>
</template>

<script>
import MachineStatus from '@/components/Serveurs/MachineStatus.vue';
import OtherInfo from '@/components/Serveurs/OtherInfo.vue';

export default {
  name: 'ServeursPage',
  components: {
    MachineStatus,
    OtherInfo,
  },
  data() {
    return {
      activeTab: 'machineStatus',
    };
  },
  methods: {
    setActiveTab(tab) {
      this.activeTab = tab;
    },
  },
};
</script>

<style scoped>
.serveurs-page {
  padding-top: 20px;
}

.tabs-onglet {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
  border-bottom: 2px solid #ccc;
}

.tab {
  cursor: pointer;
  padding: 10px 20px;
  margin: 0 10px;
  border-bottom: 2px solid transparent;
  font-weight: bold;
}

.tab.active {
  border-bottom: 2px solid #007bff;
  color: #007bff;
}

.tab:hover {
  color: #0056b3;
}
</style>
