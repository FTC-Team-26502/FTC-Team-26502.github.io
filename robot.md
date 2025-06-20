  <section class="robot-section">
    <h1>BRB Robotics</h1>
    <p>FTC Team #26502: Designing, Building, and Programming Competitive Robots</p>
    
    <div class="robot-showcase">
      <h2>Meet Our Current Robot</h2>
      <p>Our latest creation for the FTC CENTERSTAGE challenge!</p>
      <div class="robot-stats">
        <div class="stat-item">Weight: 34.2 lbs</div>
        <div class="stat-item">Height: 17.5 inches</div>
        <div class="stat-item">Drive: Mecanum</div>
        <div class="stat-item">Motors: 8</div>
        <div class="stat-item">Sensors: 12</div>
      </div>
      <p>Our robot features a precision intake system, articulated arm, and autonomous navigation with computer vision.</p>
      <a href="#" class="details-button">View Robot Gallery</a>
    </div>
    
    <div class="robot-photo-gallery">
      <h2>Robot Evolution</h2>
      <div class="gallery-tabs">
        <div class="gallery-tab active" onclick="showPhotoTab('version1')">Version 1</div>
        <div class="gallery-tab" onclick="showPhotoTab('version2')">Version 2</div>
        <div class="gallery-tab" onclick="showPhotoTab('version3')">Version 3</div>
        <div class="gallery-tab" onclick="showPhotoTab('drivebase')">Custom CAD Drivebase</div>
      </div>
      
      <div class="photo-container active" id="version1">
        <div class="photo-placeholder">
          <p>BRB Robotics - Version 1 Photo</p>
        </div>
        <div class="photo-description">
          <p>Our initial robot build focused on a sturdy and reliable drivebase with a basic linear slide mechanism. This version demonstrated at our first qualifying event featured:</p>
          <ul>
            <li>Simple 4-wheel mecanum drive</li>
            <li>Single-stage linear slide with servo gripper</li>
            <li>Basic autonomous navigation capabilities</li>
            <li>Minimal computer vision implementation</li>
          </ul>
          <p>While Version 1 had limited capabilities, it established our foundation for more advanced iterations and proved reliable in competition with minimal failures.</p>
        </div>
      </div>
      
      <div class="photo-container" id="version2">
        <div class="photo-placeholder">
          <p>BRB Robotics - Version 2 Photo</p>
        </div>
        <div class="design-section">
          <h3>V2 Robot Design Specifications</h3>
          
          <h4>Structural Design</h4>
          <p><strong>Chassis:</strong> Our robot features a compact 13.5" by 15" chassis to maximize maneuverability around the submersible.</p>
          <p><strong>Tradeoff Analysis:</strong> A bigger chassis would allow us to add a second Viper slide to attempt level 2 or 3 ascent, but a smaller chassis would have better maneuverability. We decided to sacrifice the 30 points from a third-level ascent, but we believe we can score four high-chamber specimens and a first-level ascent, which equals 43, with a smaller robot.</p>
          
          <h4>Drive Train</h4>
          <p>We implemented gearboxes with miter gears, allowing us to position one drive motor horizontally within a U-channel while mounting the other three vertically. This configuration provides robust structural support for our side panels.</p>
          <p><strong>Tradeoff Analysis:</strong> One front motor and the back motors placed vertically help us with a better weight distribution. This configuration limits the space available for the intake arm.</p>
          
          <h4>Intake</h4>
          <p>The intake uses a 3D-printed claw with a wrist on a rotating arm, connected to a viper slide moved by a 3D-printed scissor lift powered by a 188:1 motor.</p>
          <p><strong>Tradeoff Analysis:</strong> Because our small driving base limits space, we used the highest torque available from goBILDA instead of gearboxes to decrease speed. The high-torque motor makes it easier to control the extension of the horizontal slide.</p>
          <p>We built a goBILDA 4-stage viper slide with a 3D-printed claw and wrist mounted on a rotating arm to score samples in the high basket.</p>
          <p><strong>Lessons learned:</strong> the steel goBILDA viper slides add significant weight; therefore, we can not achieve a level 2 ascent or higher. Instead, we focused on designing a small and agile driving base, as well as quick specimen and sample cycles. We plan to fundraise and buy MISUMI slides made of aluminum and thus much lighter next year.</p>
          
          <h4>Hardware Failures and Weight Distribution</h4>
          <p>We have made many changes to accommodate different problems encountered during our robot design version 2.</p>
          <ul>
            <li>We addressed frequent top arm servo failures by adding software limits to prevent backward movement during the "Ready to Hang Specimen" stage and restricting the viper motor's downward range.</li>
            <li>We transitioned from swingarm odometry pods to our robot's more compact 4-bar pods. The swingarm pods, while functional, were bulky and posed challenges--particularly ensuring they were properly tucked in after the robot came off the ground. Additionally, any damage to the swingarm pods significantly impacted their performance.</li>
            <li>The switch to 4-bar pods offered several advantages. These new pods are more compact and retract vertically inside the U-channel, making them less prone to damage and easier to manage. However, they are not without drawbacks. One issue is that the wires tend to rub against the mounting U-channel, which could lead to wear over time. The most significant drawback, however, was the need to retune the PID controllers. This process proved time-consuming and required considerable effort to ensure the robot performed optimally with the new odometry system.</li>
            <li>We replaced one of our drive train's motors due to it breaking.</li>
          </ul>
          
          <p>We have had some issues with the weight distribution throughout the robot. Over time, the weight of the horizontal viper slide combined with crashing into the field walls and the submersible, and the front wheels started to lose contact with the ground.</p>
          <ul>
            <li>We mounted one of the front motors vertically to concentrate its weight above the wheel.</li>
            <li>We moved the battery to the front.</li>
            <li>We added an Omni wheel to the back of the robot to support some of the weight of the vertical slide.</li>
          </ul>
          
          <h4>Odometry and Path Planning</h4>
          <p>We evolved our autonomous navigation through three major stages:</p>
          <ol>
            <li><strong>Initial Approach:</strong> Motor encoders were used for fixed distances, which proved inadequate as they couldn't account for momentum and weight shifts.</li>
            <li><strong>Upgrade to Odometry:</strong> Used three goBILDA swing arm, and the 4-bar odometry pods for precise position and heading tracking:
              <ul>
                <li>Two vertical pods on robot edges, leaving the middle clear for claw transfers</li>
                <li>One horizontal pod at the front, positioned to avoid interference with the claw</li>
              </ul>
            </li>
            <li><strong>Road Runner Integration:</strong> Adopted the Road Runner library based on mentor advice. The tuning process involved multiple opmodes and parameter adjustments, guided by official documentation and Team 21225 Shear Force's videos.</li>
          </ol>
          
          <p>To best complement the capabilities of our alliance partners, we created two main autonomous programs. The first program collects the alliance-neutral blocks and scores them into the high basket. The second program moves three samples into the observation zone and hangs five specimens in the high chamber.</p>
          
          <h4>First Program Pseudocode</h4>
          <ul>
            <li>Start: robot on the center-left with preloaded alliance neutral sample.</li>
            <li>Robot drives to net zone</li>
            <li>Deposits sample in the high basket.</li>
            <li>Repeat three times
              <ul>
                <li>The robot turns to a sample</li>
                <li>Collects the sample in the intake</li>
                <li>Transfers the sample to the vertical claw</li>
                <li>Deposits sample</li>
              </ul>
            </li>
            <li>Drive to the submersible for first-level ascent.</li>
          </ul>
          
          <h4>Second Program Pseudocode</h4>
          <ul>
            <li>Start: robot on the center-right with the preloaded specimen in alliance color.</li>
            <li>The robot scores the specimen on the high chamber.</li>
            <li>The robot drives to the first specimen</li>
            <li>Repeat three times
              <ul>
                <li>Extend horizontal slide</li>
                <li>Push sample in observation zone</li>
              </ul>
            </li>
            <li>Repeat four times
              <ul>
                <li>Grab one specimen off the field wall</li>
                <li>Rotate 180 degrees</li>
                <li>Score specimen on the high chamber</li>
                <li>Rotate 180 degrees</li>
              </ul>
            </li>
            <li>Drive to the observation zone.</li>
          </ul>
          
          <h4>Color Sensors and Indicator Lights</h4>
          <p>We added a color sensor to our claw to prevent grabbing the wrong color. We coded the color sensor to read the sample color (red, blue, and yellow) and close if the sample's color matched the target color.</p>
          <p>We are ready to collaborate with our alliance partners to score either samples in the high basket or specimens in the high chambers. If our role is to score specimens, the claw will only close on blocks matching the alliance color. Conversely, if our role is to score samples, the claw will close on blocks of either alliance or neutral colors.</p>
          <p>When the color sensor detects a block of alliance or neutral color, the indicator lights will illuminate to display the detected color.</p>
          
          <h4>Webcam and AI</h4>
          <p>Initially, we mounted the Logitech C270 Webcam to the intake claw. However, the images captured were unfocused and did not provide sufficient visibility of the block for training the machine-learning model. Next, we mounted the camera to the end of the horizontal viper slide to address the camera's fixed focus and limited field of view. After collecting several pictures, we realized that even though the images were less blurry and captured more of the field, we could not capture angles that would clearly show the claw position relative to the block. We decided to invest in a better camera that we believed would make it more likely to capture images to train our AI successfully.</p>
          <p>After careful consideration, we decided to buy a wide-angle ELP High-Speed Wide Angle Global Shutter USB Camera Module. The images we captured with this camera were well-suited for training a machine language model.</p>
          <p><strong>Initial Plan:</strong> Our initial approach was to train a machine learning model that would take an image as input and output the target positions for the three servos controlling the intake claw. However, after visiting the Collaborative Robotics Lab at UVa and receiving feedback on our idea, we decided to switch to a pose detection approach. This new method involved detecting the orientation of a sample and calculating the servo commands based on those detections. Unfortunately, we could not implement and code this approach due to the significant amount of time spent repairing the robot.</p>
          
          <h4>Driver Controlled Enhancements</h4>
          <p>To minimize the effort made by our drivers, we implemented the following:</p>
          <ul>
            <li>Limits for the extension of vertical and horizontal slides</li>
            <li>Automatic transfer between claws</li>
            <li>Automatic positioning of the vertical claw after grabbing the specimen from the wall</li>
            <li>The robot is blocked from moving backward when it attempts to hang a specimen.</li>
            <li>The vertical slide stops at the optimal position to protect the servo of the vertical arm.</li>
          </ul>
        </div>
      </div>
      
      <div class="photo-container" id="version3">
        <div class="photo-placeholder">
          <p>BRB Robotics - Version 3 Photo (Current)</p>
        </div>
        <div class="photo-description">
          <p>Our final competition version represents our most advanced design with championship-level capabilities:</p>
          <ul>
            <li>Lightweight aluminum and carbon fiber construction</li>
            <li>Triple-stage cascading slides with 36-inch extension</li>
            <li>Dual intake systems for rapid collection</li>
            <li>Advanced articulated wrist with 270° rotation</li>
            <li>Custom-developed vision system with machine learning</li>
            <li>Sophisticated autonomous routines with adaptive behavior</li>
          </ul>
          <p>Version 3 incorporates everything we learned throughout the season and represents thousands of engineering hours. This robot has successfully competed at the state championship and is headed to the World Championship event!</p>
        </div>
      </div>
      
      <div class="photo-container" id="drivebase">
        <h3>Custom CAD Drivebase</h3>
        
        <div class="cad-model-container">
          <div class="model-instructions">Click and drag to rotate | Right-click to pan | Scroll to zoom</div>
          <canvas id="renderCanvas" touch-action="none"></canvas>
        </div>
        
        <div class="photo-description">
          <p>This is our custom-designed drivebase for next season created using CAD software. Key features include:</p>
          <ul>
            <li>Optimized weight distribution for improved balance</li>
            <li>Integrated wire management</li>
            <li>Modular mounting system for quick subsystem swapping</li>
            <li>Built-in odometry pod mounts</li>
            <li>20% lighter than our previous design</li>
          </ul>
        </div>
      </div>
    </div>
    
    <p>BRB Robotics #26502 is dedicated to engineering excellence and competing at the highest levels in FTC!</p>
  </section>

  <script src="https://cdn.babylonjs.com/babylon.js"></script>
  <script>
    function toggleInfo(id, button) {
      const infoDiv = document.getElementById(id);
      if (infoDiv.style.display === "block") {
        infoDiv.style.display = "none";
        button.innerHTML = "Learn More ▼";
      } else {
        infoDiv.style.display = "block";
        button.innerHTML = "Show Less ▲";
      }
    }
    
    function showPhotoTab(tabId) {
      // Hide all photo containers
      document.querySelectorAll('.photo-container').forEach(container => {
        container.classList.remove('active');
      });
      
      // Deactivate all tabs
      document.querySelectorAll('.gallery-tab').forEach(tab => {
        tab.classList.remove('active');
      });
      
      // Show the selected container
      document.getElementById(tabId).classList.add('active');
      
      // Activate the clicked tab
      event.currentTarget.classList.add('active');
      
      // If we're switching to the CAD tab, initialize the 3D renderer if needed
      if (tabId === 'drivebase' && !window.sceneInitialized) {
        initScene();
        window.sceneInitialized = true;
      }
    }
    
    // Add event listener for the robot gallery button
    document.querySelector('.robot-showcase .details-button').addEventListener('click', function(e) {
      e.preventDefault();
      alert('Opening robot gallery with photos from build season, competition matches, and technical details.');
    });
    
    // 3D Model rendering with BabylonJS
    function initScene() {
      const canvas = document.getElementById("renderCanvas");
      const engine = new BABYLON.Engine(canvas, true);
      
      const createScene = function() {
        // Create a scene
        const scene = new BABYLON.Scene(engine);
        scene.clearColor = new BABYLON.Color4(0.95, 0.95, 0.95, 1);
        
        // Create a camera
        const camera = new BABYLON.ArcRotateCamera("camera", -Math.PI / 2, Math.PI / 3, 5, BABYLON.Vector3.Zero(), scene);
        camera.attachControl(canvas, true);
        camera.lowerRadiusLimit = 3;
        camera.upperRadiusLimit = 10;
        
        // Create lights
        const light1 = new BABYLON.HemisphericLight("light1", new BABYLON.Vector3(0, 1, 0), scene);
        light1.intensity = 0.7;
        const light2 = new BABYLON.DirectionalLight("light2", new BABYLON.Vector3(0, -1, 1), scene);
        light2.intensity = 0.5;
        
        // Create a custom drivetrain model
        const drivebase = createDrivebaseModel(scene);
        
        // Add auto-rotation
        let autoRotate = true;
        const rotationSpeed = 0.005;
        
        scene.registerBeforeRender(function() {
          if (autoRotate) {
            drivebase.rotation.y += rotationSpeed;
          }
        });
        
        return scene;
      }
      
      // Function to create a custom 3D model of a drivetrain
      function createDrivebaseModel(scene) {
        // Create materials
        const chassisMaterial = new BABYLON.StandardMaterial("chassisMaterial", scene);
        chassisMaterial.diffuseColor = new BABYLON.Color3(0.1, 0.55, 0.1);
        chassisMaterial.specularColor = new BABYLON.Color3(0.3, 0.3, 0.3);
        
        const wheelMaterial = new BABYLON.StandardMaterial("wheelMaterial", scene);
        wheelMaterial.diffuseColor = new BABYLON.Color3(0.2, 0.2, 0.2);
        
        const motorMaterial = new BABYLON.StandardMaterial("motorMaterial", scene);
        motorMaterial.diffuseColor = new BABYLON.Color3(0.8, 0.1, 0.7);
        
        // Create main chassis base
        const mainChassis = BABYLON.MeshBuilder.CreateBox("chassis", {width: 2, height: 0.25, depth: 2}, scene);
        mainChassis.position.y = 0.125;
        mainChassis.material = chassisMaterial;
        
        // Add top plate to chassis
        const topPlate = BABYLON.MeshBuilder.CreateBox("topPlate", {width: 1.5, height: 0.1, depth: 1.5}, scene);
        topPlate.position.y = 0.3;
        topPlate.material = chassisMaterial;
        
        // Create wheels at the corners
        const wheelPositions = [
          {x: -0.85, z: -0.85}, // Front Left
          {x: 0.85, z: -0.85},  // Front Right
          {x: -0.85, z: 0.85},  // Back Left
          {x: 0.85, z: 0.85}    // Back Right
        ];
        
        wheelPositions.forEach((pos, index) => {
          // Create wheel
          const wheel = BABYLON.MeshBuilder.CreateCylinder(`wheel_${index}`, {
            height: 0.3,
            diameter: 0.6,
            tessellation: 24
          }, scene);
          
          wheel.id = "wheel";
          wheel.rotation.z = Math.PI / 2;
          wheel.position.x = pos.x;
          wheel.position.y = 0;
          wheel.position.z = pos.z;
          wheel.material = wheelMaterial;
          
          // Create motor
          const motor = BABYLON.MeshBuilder.CreateBox(`motor_${index}`, {
            width: 0.4,
            height: 0.4,
            depth: 0.5
          }, scene);
          
          motor.id = "motor";
          motor.position.x = pos.x - (index % 2 === 0 ? -0.3 : 0.3);
          motor.position.y = 0.2;
          motor.position.z = pos.z;
          motor.material = motorMaterial;
        });
        
        // Create central hub
        const hub = BABYLON.MeshBuilder.CreateCylinder("hub", {
          height: 0.25,
          diameter: 0.8,
          tessellation: 16
        }, scene);
        hub.position.y = 0.4;
        hub.material = chassisMaterial;
        
        // Create simple rod supports
        const supportPositions = [
          {x: 0, z: -0.8},  // Front
          {x: 0, z: 0.8},   // Back
          {x: -0.8, z: 0},  // Left
          {x: 0.8, z: 0}    // Right
        ];
        
        supportPositions.forEach((pos) => {
          const support = BABYLON.MeshBuilder.CreateCylinder("support", {
            height: 0.5,
            diameter: 0.1,
            tessellation: 8
          }, scene);
          
          support.position.x = pos.x;
          support.position.y = 0.25;
          support.position.z = pos.z;
          support.material = chassisMaterial;
        });
        
        // Group all drivebase components under a parent node
        const drivebase = new BABYLON.TransformNode("drivebase");
        for (let meshIndex = 0; meshIndex < scene.meshes.length; meshIndex++) {
          scene.meshes[meshIndex].parent = drivebase;
        }
        
        return drivebase;
      }
      
      const scene = createScene();
      
      engine.runRenderLoop(function() {
        scene.render();
      });
      
      window.addEventListener("resize", function() {
        engine.resize();
      });
    }
  </script>
