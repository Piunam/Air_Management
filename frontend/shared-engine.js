/**
 * AERO-OPS Distributed Data Model
 */
window.AeroState = {
    flights: [
        { id: 'LH-432', origin: 'Frankfurt (FRA)', time: '12:55', gate: 'A01', status: 'Airborne' },
        { id: 'SQ-021', origin: 'Singapore (SIN)', time: '13:15', gate: 'A02', status: 'Airborne' },
        { id: 'AA-241', origin: 'Dallas (DFW)', time: '14:20', gate: 'A03', status: 'Landed' },
        { id: 'BA-098', origin: 'London (LHR)', time: '14:55', gate: '--', status: 'Delayed' },
        { id: 'EK-202', origin: 'Dubai (DXB)', time: '15:10', gate: 'A04', status: 'Airborne' }
    ],
    resources: {
        desks: [
            { id: 'Counters 01-05', airline: 'Air India', load: 'Heavy', status: 'Active' },
            { id: 'Counters 06-10', airline: 'Lufthansa', load: 'Optimal', status: 'Active' },
            { id: 'Counters 11-12', airline: 'British Airways', load: 'None', status: 'Standby' }
        ],
        carousels: [
            { id: 'Belt Loop 1', flight: 'AA-241', bags: 184, status: 'Processing' },
            { id: 'Belt Loop 2', flight: '--', bags: 0, status: 'Clear' }
        ]
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const clockNode = document.getElementById('digital-clock');
    if (!clockNode) return;

    function renderTime() {
        const timeObj = new Date();
        clockNode.textContent = timeObj.toISOString().substr(11, 8) + ' UTC';
    }
    
    renderTime();
    setInterval(renderTime, 1000);
});