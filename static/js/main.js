

$( () => {
    const bmiSlider = document.getElementById('personBMI');
    const bmiValueDisplay = document.getElementById('bmiValue');
    const glucoseSlider = document.getElementById('personGlucose');
    const glucoseValueDisplay = document.getElementById('glucoseValue');
    const cylinderSlider = document.getElementById('carCylinders');
    const cylinderValueDisplay = document.getElementById('cylindersValue');
    const horsepowerSlider = document.getElementById('carHorsepower');
    const horsepowerValueDisplay = document.getElementById('horsepowerValue');
    const weightSlider = document.getElementById('carWeight');
    const weightValueDisplay = document.getElementById('weightValue');
    const carYearSlider = document.getElementById('carYear');
    const carYearValueDisplay = document.getElementById('carYearValue');

    if (bmiSlider && glucoseSlider) {
        bmiValueDisplay.textContent = parseFloat(bmiSlider.value).toFixed(1);
        glucoseValueDisplay.textContent = parseInt(glucoseSlider.value);

        bmiSlider.oninput = function() {
            const roundedValue = parseFloat(bmiSlider.value).toFixed(1);
            bmiValueDisplay.textContent = roundedValue;
        }

        glucoseSlider.oninput = function() {
            glucoseValueDisplay.textContent = parseInt(glucoseSlider.value);
        }
    }

    else if (cylinderSlider && horsepowerSlider && weightSlider && carYearSlider){
        cylinderValueDisplay.textContent = parseInt(cylinderSlider.value);
        horsepowerValueDisplay.textContent = parseFloat(horsepowerSlider.value).toFixed(2);
        weightValueDisplay.textContent = parseInt(weightSlider.value);
        carYearValueDisplay.textContent = parseInt(carYearSlider.value);

        cylinderSlider.oninput = function() {
            cylinderValueDisplay.textContent = parseInt(cylinderSlider.value);
        }

        horsepowerSlider.oninput = function() {
            horsepowerValueDisplay.textContent = parseFloat(horsepowerSlider.value).toFixed(1);
        }

        weightSlider.oninput = function()   {
            weightValueDisplay.textContent = parseInt(weightSlider.value);
        }

        carYearSlider.oninput = function() {
            carYearValueDisplay.textContent = parseInt(carYearSlider.value);
        }
    }
});