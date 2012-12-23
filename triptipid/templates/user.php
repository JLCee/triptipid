<?php include 'header.php'; ?>
			<div id="user" class="main dashboard">
				<div class="content">
<?php include 'sidebar-dashboard.php'; ?>
					<header class="content-header">
						<h1 class="title">My Profile</h1>
					</header>
					<section id="user-content" class="dashboard-content">
						<div id="user-left">
							<div id="user-image">
								<h3>My Display Picture</h3>
								<div class="image"></div>
								<button>Upload New</button>
							</div>
							<div id="user-social">
								<h3>My Social Networks</h3>
								<ul class="networks">
									<li></li>
									<li></li>
									<li></li>
									<li></li>
									<li></li>
									<li></li>
									<li></li>
									<li></li>
								</ul>
							</div>
						</div>
						<div id="user-right">
							<div id="user-stats">
								<h3>My Account Statistics</h3>
								<div class="posts">
									<div class="icon"></div>
									<div class="num">1,023</div>
								</div>
								<div class="rating">
									<div class="text">Average Rating:</div>
									<div class="stars">X X X X X</div>
								</div>
							</div>
							<div id="user-details">
								<h3>My Account Details</h3>
								<ul>
									<li>
										<label>Name</label>
										<div class="input-append">
											<input type="text" placeholder="Gabriel Fabia">
											<button class="add-on">Edit</button>
										</div>
									</li>
									<li>
										<label>Username</label>
										<div class="input-username input-prepend input-append">
											<span class="add-on">triptipid.com/</span>
											<input type="text" placeholder="gabfabia">
											<button class="add-on">Edit</button>
										</div>
									</li>
									<li>
										<label>Email Address</label>
										<div class="input-append">
											<input type="text" placeholder="gfabia@gmail.com">
											<button class="add-on">Edit</button>
										</div>
									</li>
									<li>
										<label>Password</label>
										<div class="input-append">
											<input type="text" placeholder="gabfabia">
											<button class="add-on">Edit</button>
										</div>
									</li>
								</ul>
							</div>
						</div>
					</section>
				</div>
			</div>
			<div id="bgrow-dashboard"></div>
<?php include 'footer.php'; ?>