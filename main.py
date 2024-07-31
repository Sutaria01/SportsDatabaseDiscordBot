import discord
import os
from discord.ext import commands
from models import (
    Users,
    Address,
    Admins,
    Plans,
    Subscriptions,
    EnrollTo,
    HealthStatus,
    LoginLogs,
    Events,
    SportsTimetable,
    Managers,
    Scouts,
    Advertisements,
    Agents,
)

# Load Discord Token from environment variable
TOKEN = os.environ["DISCORD_TOKEN"]

# Intents for all events
intents = discord.Intents.all()

# Initialize bot with custom prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Define functions to execute each SQL query as a Discord command

@bot.command(name="fetch_user_address", description="Fetch users with their addresses.")
async def _fetch_user_address(ctx):
    try:
        users_with_address = Address.fetch_users_with_address()
        for user in users_with_address:
            await ctx.send(
                f"User ID: {user['userId']}, Username: {user['username']}, Email: {user['email']}, Address: {user['streetName']}, {user['state']}, {user['city']}, {user['zipcode']}"
            )
    except Exception as e:
        await ctx.send(f"Error fetching user addresses: {e}")

@bot.command(name="fetch_user_subscriptions", description="Fetch users with their subscriptions and plans.")
async def _fetch_user_subscriptions(ctx):
    try:
        user_subscriptions = Subscriptions.fetch_users_enrolled_in_plans()
        for subscription in user_subscriptions:
            await ctx.send(
                f"Username: {subscription['username']}, Plan: {subscription['planName']}, Purchase Date: {subscription['purchaseDate']}, Expiration Date: {subscription['expirationDate']}, Renewal Status: {subscription['renewalStatus']}"
            )
    except Exception as e:
        await ctx.send(f"Error fetching user subscriptions: {e}")

@bot.command(name="fetch_user_health_status", description="Fetch users with their health status.")
async def _fetch_user_health_status(ctx):
    try:
        user_health_status = HealthStatus.fetch_user_health_status()
        for health_status in user_health_status:
            await ctx.send(
                f"Username: {health_status['username']}, Calorie: {health_status['calorie']}, Height: {health_status['height']}, Weight: {health_status['weight']}, Fat Index: {health_status['fatIndex']}, Suggestions: {health_status['suggestions']}, Date Recorded: {health_status['dateRecorded']}"
            )
    except Exception as e:
        await ctx.send(f"Error fetching user health status: {e}")

@bot.command(name="fetch_user_login_logs", description="Fetch users with their login logs.")
async def _fetch_user_login_logs(ctx):
    try:
        user_login_logs = LoginLogs.fetch_user_login_logs()
        for login_log in user_login_logs:
            await ctx.send(
                f"Username: {login_log['username']}, Action: {login_log['action']}, Timestamp: {login_log['timestamp']}"
            )
    except Exception as e:
        await ctx.send(f"Error fetching user login logs: {e}")

@bot.command(name="register_user", description="Register a new user.")
async def _register_user(ctx, username, email, gender, mobile, dob, joining_date):
    try:
        success = Users.register_user(username, email, gender, mobile, dob, joining_date)
        if success:
            await ctx.send("User registered successfully!")
        else:
            await ctx.send("Error registering user.")
    except Exception as e:
        await ctx.send(f"Error registering user: {e}")

@bot.command(name="add_address", description="Add an address to a user profile.")
async def _add_address(ctx, user_id, street_name, state, city, zipcode):
    try:
        success = Address.add_address(user_id, street_name, state, city, zipcode)
        if success:
            await ctx.send("Address added successfully!")
        else:
            await ctx.send("Error adding address.")
    except Exception as e:
        await ctx.send(f"Error adding address: {e}")

@bot.command(name="add_admin", description="Add an admin to the system.")
async def _add_admin(ctx, username, passkey, full_name):
    try:
        success = Admins.add_admin(username, passkey, full_name)
        if success:
            await ctx.send("Admin added successfully!")
        else:
            await ctx.send("Error adding admin.")
    except Exception as e:
        await ctx.send(f"Error adding admin: {e}")

@bot.command(name="add_plan", description="Add a new plan to the system.")
async def _add_plan(ctx, plan_name, description, validity, amount):
    try:
        success = Plans.add_plan(plan_name, description, validity, amount)
        if success:
            await ctx.send("Plan added successfully!")
        else:
            await ctx.send("Error adding plan.")
    except Exception as e:
        await ctx.send(f"Error adding plan: {e}")

@bot.command(name="enroll_user", description="Enroll a user to a plan.")
async def _enroll_user(ctx, user_id, plan_id, purchase_date, expiration_date, renewal_status):
    try:
        success = Subscriptions.enroll_user(user_id, plan_id, purchase_date, expiration_date, renewal_status)
        if success:
            await ctx.send("User enrolled successfully!")
        else:
            await ctx.send("Error enrolling user.")
    except Exception as e:
        await ctx.send(f"Error enrolling user: {e}")

@bot.command(name="add_health_status", description="Add health status to a user profile.")
async def _add_health_status(ctx, user_id, calorie, height, weight, fat_index, suggestions, date_recorded):
    try:
        success = HealthStatus.add_health_status(user_id, calorie, height, weight, fat_index, suggestions, date_recorded)
        if success:
            await ctx.send("Health status added successfully!")
        else:
            await ctx.send("Error adding health status.")
    except Exception as e:
        await ctx.send(f"Error adding health status: {e}")

@bot.command(name="add_login_log", description="Add a login log for a user.")
async def _add_login_log(ctx, user_id, action, timestamp):
    try:
        success = LoginLogs.add_login_log(user_id, action, timestamp)
        if success:
            await ctx.send("Login log added successfully!")
        else:
            await ctx.send("Error adding login log.")
    except Exception as e:
        await ctx.send(f"Error adding login log: {e}")

@bot.command(name="add_manager", description="Add a manager to the system.")
async def _add_manager(ctx, name):
    try:
        success = Managers.add_manager(name)
        if success:
            await ctx.send("Manager added successfully!")
        else:
            await ctx.send("Error adding manager.")
    except Exception as e:
        await ctx.send(f"Error adding manager: {e}")

@bot.command(name="add_scout", description="Add a scout to the system.")
async def _add_scout(ctx, name):
    try:
        success = Scouts.add_scout(name)
        if success:
            await ctx.send("Scout added successfully!")
        else:
            await ctx.send("Error adding scout.")
    except Exception as e:
        await ctx.send(f"Error adding scout: {e}")

@bot.command(name="add_advertisement", description="Add an advertisement to the system.")
async def _add_advertisement(ctx, name):
    try:
        success = Advertisements.add_advertisement(name)
        if success:
            await ctx.send("Advertisement added successfully!")
        else:
            await ctx.send("Error adding advertisement.")
    except Exception as e:
        await ctx.send(f"Error adding advertisement: {e}")

@bot.command(name="add_agent", description="Add an agent to the system.")
async def _add_agent(ctx, name):
    try:
        success = Agents.add_agent(name)
        if success:
            await ctx.send("Agent added successfully!")
        else:
            await ctx.send("Error adding agent.")
    except Exception as e:
        await ctx.send(f"Error adding agent: {e}")
        
@bot.command(name="add_sports_event", description="Add a sports event to the system.")
async def _add_sports_event(ctx, event_name, event_date, event_time, event_location, event_description):
    try:
        success = Events.add_sports_event(event_name, event_date, event_time, event_location, event_description)
        if success:
            await ctx.send("Sports event added successfully!")
        else:
            await ctx.send("Error adding sports event.")

    except Exception as e:
        await ctx.send(f"Error adding sports event: {e}")
# Run the bot
bot.run(TOKEN)
