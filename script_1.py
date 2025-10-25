
# ============================================================================
# FINAL OPTIMIZED SIMULATION ENGINE
# ============================================================================

class FinalOptimizedSimulation:
    """Realistic ITS latency + Literature-aligned IRS gain"""
    
    def __init__(self):
        self.mobility = OptimizedMobilityModel(num_vehicles=50, num_rsus=15)
        self.channel = RealisticChannel()
        self.irs = CalibratedIRS(num_elements=50)
        self.compressor = FastSemanticCompressor()
        self.mac = OptimizedMAC()
        
    def simulate_transmission(self, vehicle, target, offload_mode='semantic_irs'):
        result = {'vehicle_id': vehicle.id, 'mode': offload_mode}
        
        raw_data_kb = vehicle.sensor_data_size
        result['raw_data_kb'] = raw_data_kb
        
        # Semantic compression
        if 'semantic' in offload_mode:
            compressed_kb, _, compress_time_ms = self.compressor.compress(raw_data_kb)
            result['compressed_kb'] = compressed_kb
            result['compression_time_ms'] = compress_time_ms
            data_to_send_kb = compressed_kb
        else:
            data_to_send_kb = raw_data_kb
            result['compressed_kb'] = raw_data_kb
            result['compression_time_ms'] = 0
        
        # Find closest RSU (realistic deployment)
        distances = [np.linalg.norm(vehicle.position - rsu.position) 
                    for rsu in self.mobility.rsus]
        distance = min(distances)  # Use closest RSU
        distance = min(distance, 250)  # Clip to realistic V2I range
        result['distance_m'] = distance
        
        # IRS enhancement
        if 'irs' in offload_mode:
            irs_gain_db = self.irs.adaptive_beamforming([vehicle.position], target.position)
            result['irs_gain_db'] = irs_gain_db
        else:
            irs_gain_db = 0
            result['irs_gain_db'] = 0
        
        # Wireless channel
        tx_power_dbm = 23
        snr_db = self.channel.calculate_snr(tx_power_dbm, distance, irs_gain_db)
        datarate_mbps = self.channel.calculate_datarate_mbps(snr_db)
        result['snr_db'] = snr_db
        result['datarate_mbps'] = datarate_mbps
        
        # MAC delay (optimized)
        mac_delay_ms = self.mac.calculate_mac_delay_ms(data_to_send_kb, datarate_mbps, 
                                                        num_contending=3)
        result['mac_delay_ms'] = mac_delay_ms
        
        # Transmission delay
        tx_delay_ms = (data_to_send_kb * 8 * 1024) / (datarate_mbps * 1000)
        result['tx_delay_ms'] = tx_delay_ms
        
        # Propagation delay (negligible for short distances)
        prop_delay_ms = (distance / 3e8) * 1000
        result['prop_delay_ms'] = prop_delay_ms
        
        # Processing at RSU/MEC (optimized)
        processing_delay_ms = 3.0  # Fast MEC
        result['processing_delay_ms'] = processing_delay_ms
        
        # Handover (rare in dense deployment)
        handover_delay_ms = 50.0 if np.random.rand() < 0.05 else 0  # 5% probability
        result['handover_delay_ms'] = handover_delay_ms
        
        # Total latency
        total_latency_ms = (result.get('compression_time_ms', 0) + mac_delay_ms + 
                           tx_delay_ms + prop_delay_ms + processing_delay_ms + handover_delay_ms)
        result['total_latency_ms'] = total_latency_ms
        
        # Energy
        tx_energy_mj = (tx_delay_ms / 1000) * (10 ** (tx_power_dbm / 10))
        compress_energy_mj = 40 if 'semantic' in offload_mode else 0  # Optimized LLM
        irs_energy_mj = 1.5 if 'irs' in offload_mode else 0
        result['energy_consumption_mj'] = tx_energy_mj + compress_energy_mj + irs_energy_mj
        
        # Success (high SNR with IRS)
        result['packet_success'] = snr_db > 3.0
        
        return result
    
    def run_full_scenario(self):
        print(f"\n{'='*70}")
        print("RUNNING FINAL OPTIMIZED SIMULATION")
        print(f"{'='*70}")
        
        modes = ['raw', 'semantic', 'semantic_irs']
        results_by_mode = {mode: [] for mode in modes}
        
        for mode in modes:
            print(f"\n🔄 Mode: {mode.upper()}")
            for i in range(150):  # More samples for better statistics
                vehicle = np.random.choice(self.mobility.vehicles)
                target = np.random.choice(self.mobility.rsus)
                result = self.simulate_transmission(vehicle, target, mode)
                results_by_mode[mode].append(result)
                if (i+1) % 50 == 0:
                    print(f"   Progress: {i+1}/150")
        
        return results_by_mode

print("\n" + "="*70)
print("STARTING FINAL OPTIMIZED SIMULATION")
print("="*70)

sim_final_opt = FinalOptimizedSimulation()
results_final_opt = sim_final_opt.run_full_scenario()

print("\n✅ SIMULATION COMPLETE!")
