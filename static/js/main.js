

$( () => {
    const bmiSlider = document.getElementById('personBMI');
    const bmiValueDisplay = document.getElementById('bmiValue');
    const glucoseSlider = document.getElementById('personGlucose');
    const glucoseValueDisplay = document.getElementById('glucoseValue');

    bmiValueDisplay.textContent = parseFloat(bmiSlider.value).toFixed(1);
    glucoseValueDisplay.textContent = parseInt(glucoseSlider.value);

    bmiSlider.oninput = function() {
        const roundedValue = parseFloat(bmiSlider.value).toFixed(1);
        bmiValueDisplay.textContent = roundedValue;
    }

    glucoseSlider.oninput = function() {
        glucoseValueDisplay.textContent = parseInt(glucoseSlider.value);
    }
});