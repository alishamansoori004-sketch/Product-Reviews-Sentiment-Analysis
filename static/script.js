// ===========================
// Dark / Light Mode
// ===========================

console.log("script.js is running");
const toggle = document.getElementById("theme-toggle");

if (toggle) {
    toggle.addEventListener("click", function () {
        document.body.classList.toggle("light");

        if (document.body.classList.contains("light")) {
            toggle.innerHTML = "🌙";
        } else {
            toggle.innerHTML = "☀️";
        }
    });
}

// ===========================
// Progress Bar Animation
// ===========================

const bar = document.getElementById("progressBar");

if (bar) {

    const width = parseFloat(bar.dataset.width) || 0;

    bar.style.width = "0%";

    setTimeout(function () {
        bar.style.width = width + "%";
    }, 300);

}

// ===========================
// Prediction Chart
// ===========================

const canvas = document.getElementById("probChart");

if (canvas) {

    const labelsInput = document.getElementById("labels");
    const scoresInput = document.getElementById("scores");

    if (labelsInput && scoresInput) {

        const labels = JSON.parse(labelsInput.value);
        const scores = JSON.parse(scoresInput.value);

        new Chart(canvas, {

            type: "bar",

            data: {

                labels: labels,

                datasets: [{

                    label: "Probability (%)",

                    data: scores,

                    backgroundColor: [
                        "#22c55e",
                        "#f59e0b",
                        "#ef4444"
                    ],

                    borderRadius: 10

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                plugins: {

                    legend: {
                        display: false
                    }

                },

                scales: {

                    y: {

                        beginAtZero: true,
                        max: 100

                    }

                }

            }

        });

    }

}

// ===========================
// Sentiment Distribution Chart
// ===========================

const sentimentCanvas = document.getElementById("sentimentChart");

if (sentimentCanvas) {

    const positive = parseInt(
        sentimentCanvas.dataset.positive
    ) || 0;

    const neutral = parseInt(
        sentimentCanvas.dataset.neutral
    ) || 0;

    const negative = parseInt(
        sentimentCanvas.dataset.negative
    ) || 0;

    new Chart(sentimentCanvas, {

        type: "doughnut",

        data: {

            labels: [
                "Positive",
                "Neutral",
                "Negative"
            ],

            datasets: [{

                data: [
                    positive,
                    neutral,
                    negative
                ],

                backgroundColor: [
                    "#22c55e",
                    "#f59e0b",
                    "#ef4444"
                ],

                borderWidth: 0,

                hoverOffset: 10

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            cutout: "65%",

            plugins: {

                legend: {

                    position: "bottom",

                    labels: {

                        padding: 20,

                        font: {
                            size: 14
                        }

                    }

                }

            }

        }

    });

}

// ===========================
// AI Typing Animation
// ===========================

const form = document.getElementById("reviewForm");
const btn = document.getElementById("analyzeBtn");

if (form && btn) {

    form.addEventListener("submit", function () {

    document.getElementById("loadingScreen").style.display="flex";

    btn.disabled=true;

    btn.innerHTML="🤖 Analyzing...";

});
}

// ==========================
// Voice Recognition
// ==========================

const voiceBtn = document.getElementById("voiceBtn");
const textarea = document.querySelector("textarea");

if (voiceBtn && textarea) {

    const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    if (SpeechRecognition) {

        const recognition = new SpeechRecognition();

        recognition.lang = "en-US";
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        voiceBtn.addEventListener("click", function () {

            recognition.start();

            voiceBtn.innerHTML = "🎙 Listening...";
            voiceBtn.disabled = true;

        });

        recognition.onresult = function (event) {

            const transcript = event.results[0][0].transcript;

            textarea.value = transcript;

        };

        recognition.onend = function () {

            voiceBtn.innerHTML = "🎤 Speak";
            voiceBtn.disabled = false;

        };

        recognition.onerror = function () {

            alert("Voice recognition failed. Please try again.");

            voiceBtn.innerHTML = "🎤 Speak";
            voiceBtn.disabled = false;

        };

    } else {

        voiceBtn.style.display = "none";
        console.log("Speech Recognition is not supported in this browser.");

    }

}


// ==========================
// AI Particle Background
// ==========================

window.addEventListener("load", () => {

    if (typeof particlesJS === "undefined") {
        console.error("Particles.js not loaded");
        return;
    }

    console.log("Particles Loaded");

    particlesJS("particles-js", {

        particles: {

            number: {
                value: 80,
                density: {
                    enable: true,
                    value_area: 800
                }
            },

            color: {
                value: "#ffffff"
            },

            shape: {
                type: "circle"
            },

            opacity: {
                value: 0.5,
                random: true
            },

            size: {
                value: 3,
                random: true
            },

            line_linked: {
                enable: true,
                distance: 150,
                color: "#ffffff",
                opacity: 0.4,
                width: 1
            },

            move: {
                enable: true,
                speed: 2
            }

        },

        interactivity: {

            detect_on:"canvas",

            events:{

                onhover:{
                    enable:true,
                    mode:"repulse"
                },

                onclick:{
                    enable:true,
                    mode:"push"
                }

            }

        },

        retina_detect:true

    });

});

// Auto Scroll to Result
window.addEventListener("load", function () {

    const result = document.querySelector(".result");

    if(result){
        result.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }

});