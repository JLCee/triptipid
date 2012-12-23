<?php include 'header.php'; ?>
			<div id="create" class="main dashboard">
				<div class="content">
<?php include 'sidebar-dashboard.php'; ?>
					<header class="content-header">
						<!--div class="breadcrumb">
							<ul>
								<li><a href="#">Dasboard</a></li>
								<li class="current"><a href="#">Create Itinerary</a></li>
							</ul>
						</div-->
						<h1 class="title">Create Itinerary</h1>
					</header>
					<section id="create-content" class="dashboard-content">
						<div id="steps">
							<ul class="bullets">
								<li class="current">1</li>
								<li>2</li>
								<li>3</li>
								<li>4</li>
							</ul>
							<form>
								<ul class="step-content">
									<!--li class="step-1">
										<h1>General</h1>
										<label for="from">From</label>
										<input type="text" placeholder="Coming from...">
										<label for="to">To</label>
										<input type="text" placeholder="Going to...">
										<label for="persons">Person(s)</label>
										<input type="text" placeholder="1">
										<label for="transportation">Transportation</label>
										<select name="transporatation">
											<option value="public">Public</option>
											<option value="private">Private</option>
										</select>
									</li-->
									<li class="step-2">
										<ul class="days">
											<li class="day day-1">
												<div class="day-num"><h2>Day 1</h2></div>
												<div class="tabs">
													<div class="itinerary"></div>
													<div class="cost current"></div>
													<div class="hide"></div>
												</div>
												<div class="cost-info">
													<table>
														<thead>
															<tr>
																<td>Activity</td>
																<td>Activity Cost</td>
																<td>Costing Type</td>
																<td></td>
															</tr>
														</thead>
														<tbody>
															<tr>
																<td class="activity">
																	<input type="text" name="day1-activity" placeholder="What you're paying for">
																</td>
																<td class="cost">
																	<input type="text" name="cost" placeholder="How much is it?">
																</td>
																<td class="costtype">
																	<select name="day1-costtype">
																		<option value="individual">Individual</option>
																		<option value="group">Group</option>
																	</select>
																</td>
																<td class="delete">
																	<button></button>
																</td>
															</tr>
														</tbody>
														<tfoot>
															<tr>
																<td class="addcost">
																	<span>Add another cost: <button></button></span>
																</td>
																<td class="totalcost" colspan="3">
																	<div class="single iconlabel">
																		<div class="icon"></div>
																		<span class="label">7,350</span>
																	</div>
																	<div class="group iconlabel">
																		<div class="icon"></div>
																		<span class="label">7,350</span>
																	</div>
																</td>
															</tr>
														</tfoot>
													</table>
												</div>
												<!--div class="itinerary-info">
													<table>
														<thead>
															<tr>
																<td></td>
																<td>Time Start</td>
																<td>Short Description</td>
																<td></td>
															</tr>
														</thead>
														<tbody>
															<tr>
																<td class="icon">
																	<div></div>
																</td>
																<td class="time">
																	<select name="day1-time1">
																		<option value="12:00 AM">12:00 AM</option>
																		<option value="1:00 AM">1:00 AM</option>
																		<option value="2:00 AM">2:00 AM</option>
																		<option value="3:00 AM">3:00 AM</option>
																	</select>
																</td>
																<td class="description">
																	<input type="text" name="day1-description1" placeholder="Add a description...">
																</td>
																<td class="order">
																	<div></div>
																</td>
															</tr>
															<tr>
																<td class="label" colspan="2">Location:</td>
																<td class="description"><input type="text" name="day1-location" placeholder="Name of the place..."></td>
																<td></td>
															</tr>
															<tr>
																<td class="label" colspan="2">Address:</td>
																<td class="description"><input type="text" name="day1-address" placeholder="Street Address"></td>
																<td></td>
															</tr>
															<tr>
																<td class="label" colspan="2">Tel. No.:</td>
																<td class="description"><input type="text" name="day1-telno" placeholder="Telephone Number"></td>
																<td></td>
															</tr>
															<tr>
																<td class="label activitylabel" colspan="2">Add an activity:</td>
																<td class="activitybuttons" colspan="2">
																	<ul>
																		<li></li>
																		<li></li>
																		<li></li>
																		<li></li>
																		<li></li>
																		<li></li>
																	</ul>
																</td>
															</tr>
														</tbody>
													</table>
												</div-->
											</li>
										</ul>
										<button>Add Day</button>
									</li>
									<!--li class="step-3">
										
									</li-->
									<!--li class="step-4">
										
									</li-->
								</ul>
							</form>
						</div>
					</section>
				</div>
			</div>
<?php include 'footer.php'; ?>